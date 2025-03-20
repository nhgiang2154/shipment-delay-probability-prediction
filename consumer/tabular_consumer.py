import argparse
import pika

parser = argparse.ArgumentParser()
parser.add_argument(
    "-b",
    "--rabbitmq_server",
    default="localhost",
    help="Where the RabbitMQ server is",
)
parser.add_argument(
    "-q",
    "--queue_name",
    default="alicpp_records",
    help="The name of the RabbitMQ queue to consume from",
)

args = parser.parse_args()

def callback(ch, method, properties, body):
    """
    Callback function to process messages from the queue.
    Args:
        ch (BlockingChannel): The channel object.
        method (spec.Basic.Deliver): Method frame with delivery information.
        properties (spec.BasicProperties): Properties of the message.
        body (bytes): The message body.
    """
    print(f"Received message: {body}")
    # Process the message here
    # For example, you can convert the body to a dictionary if it's JSON
    # message = json.loads(body)
    # print(message)

def consume_messages(server, queue_name):
    """
    Consumes messages from a RabbitMQ queue.
    Args:
        server (str): The hostname or IP address of the RabbitMQ server.
        queue_name (str): The name of the queue to consume messages from.
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=server))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    print(f"Waiting for messages in queue: {queue_name}. To exit press CTRL+C")

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()

if __name__ == "__main__":
    parsed_args = vars(args)
    server = parsed_args["rabbitmq_server"]
    queue_name = parsed_args["queue_name"]

    consume_messages(server, queue_name)