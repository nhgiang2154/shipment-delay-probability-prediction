import argparse
import json
from datetime import datetime
from time import sleep

import pandas as pd
import numpy as np
import pika
import joblib

parser = argparse.ArgumentParser()
parser.add_argument(
    "-m",
    "--mode",
    default="setup",
    choices=["setup", "teardown"],
    help="Whether to setup or teardown a RabbitMQ queue with driver stats events. Setup will teardown before beginning emitting events.",
)
parser.add_argument(
    "-b",
    "--rabbitmq_server",
    default="localhost",
    help="Where the RabbitMQ server is",
)

args = parser.parse_args()

def create_queue(channel, queue_name):
    # Create queue if not exists
    try:
        channel.queue_declare(queue=queue_name, durable=True)
        print(f"A new queue {queue_name} has been created!")
    except Exception as e:
        print(f"Queue {queue_name} already exists. Skipping creation! Error: {e}")
        pass

# Load the models
regression_model = joblib.load("Polynomial Regression_pipeline.pkl")
tree_model = joblib.load("Decision Tree_pipeline.pkl")
random_forest_model = joblib.load("Random Forest_pipeline.pkl")
xgb_model = joblib.load("XGBoost_pipeline.pkl")

def create_streams(server, queue_name):
    """
    Establishes a connection to a RabbitMQ server, creates a queue if it doesn't exist, 
    and continuously sends messages to the queue with data sampled from a CSV file.
    Args:
        server (str): The hostname or IP address of the RabbitMQ server.
        queue_name (str): The name of the queue to which messages will be sent.
    Raises:
        Exception: If the connection to the RabbitMQ server cannot be established after multiple attempts.
    Notes:
        - The function attempts to establish a connection to the RabbitMQ server up to 10 times, 
          waiting 10 seconds between each attempt.
        - The data is read from a CSV file named 'data_sample.csv' located in the same directory.
        - Each message sent to the queue is a JSON object containing a record from the CSV file 
          with the 'created' and 'datetime' fields updated to the current timestamp.
        - Messages are sent to the queue every 2 seconds.
    """
    connection = None
    channel = None
    for _ in range(10):
        try:
            crd = pika.credentials.PlainCredentials('guest', 'guest') # Create credentials object with username and password like in docker-compose.yml
            port = 5672 # Default port for RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=server, port=port, credentials=crd))
            channel = connection.channel()
            print("SUCCESS: instantiated RabbitMQ connection and channel")
            break
        except Exception as e:
            print(
                f"Trying to instantiate connection and channel with RabbitMQ server {server} with error {e}"
            )
            sleep(10)
            pass
    
    df = pd.read_csv("C:/Users/Admin/Downloads/shipment/docker-assets/producer/tabular_data.csv")

    # Create a new queue for this device id if not exists
    create_queue(channel, queue_name=queue_name)
    while True:
        record = df.sample(1).to_dict(orient='records')[0]
        # Make event one more year recent to simulate fresher data
        record["created"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record["datetime"] = record["created"] # for simple purpose

        # Apply the models to the data
        input_features = list(regression_model.feature_names_in_)
        record_df = pd.DataFrame([record])[input_features]
        
        record["regression_prediction"] = regression_model.predict(record_df)[0]
        record["tree_prediction"] = tree_model.predict(record_df)[0]
        record["random_forest_prediction"] = random_forest_model.predict(record_df)[0]
        record["xgb_prediction"] = xgb_model.predict(record_df)[0]

        # Send messages to this queue
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(record, default=lambda x: float(x) if isinstance(x, (np.float32, np.float64)) else x),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(record)
        sleep(2)

def teardown_queue(queue_name, server="localhost"):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=server))
        channel = connection.channel()
        channel.queue_delete(queue=queue_name)
        print(f"Queue {queue_name} deleted")
    except Exception as e:
        print(str(e))
        pass

if __name__ == "__main__":
    parsed_args = vars(args)
    mode = parsed_args["mode"]
    server = parsed_args["rabbitmq_server"]
    # Get queue name for this device
    queue_name = 'alicpp_records'
    # Tear down all previous streams
    print("Tearing down all existing queues!")
    try:
        teardown_queue(f"{queue_name}", server)
    except Exception as e:
        print(f"Queue {queue_name} does not exist. Skipping...!")

    if mode == "setup":
        create_streams(server, queue_name)
