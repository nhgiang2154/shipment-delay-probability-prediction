# RabbitMQ Demo

This project demonstrates how to set up RabbitMQ producers and consumers using Docker. The project includes examples for handling CSV data, text data, and image data.

**Remember:** This repository handles the "plumbing" - getting data from point A to point B reliably. The actual ML processing is up to you and should be tailored to your specific use case.

## Prerequisites

- Docker
- Docker Compose
- Python 3.9+

## Project Structure

```txt
/rabbitMQ
├── docker-compose.yml       # Docker Compose file to set up RabbitMQ and producer services
├── requirements_dev.txt     
├── producer
│   ├── Dockerfile           # Dockerfile to build the producer image (for tabular data only)
│   ├── tabular_data.csv             # Sample data file for the `tabular` producer
│   ├── stream_tabular_ingestion.py          # Script to produce messages to RabbitMQ
│   ├── stream_image_ingestion.py  # Script to produce `image` data to RabbitMQ
│   ├── stream_text_ingestion.py   # Script to produce `text` data to RabbitMQ
│   └── images               # Directory containing sample images
│       ├── image1.jpeg
│       ├── image2.jpeg
│       └── ...
└── consumer
    ├── tabular_consumer.py          # Script to consume tabular data from RabbitMQ
    ├── image_consumer.py    # Script to consume image data from RabbitMQ
    └── text_consumer.py     # Script to consume text data from RabbitMQ
```


### Why RabbitMQ for ML?

RabbitMQ helps solve common challenges in ML pipelines:

- Real-time Processing: Stream data directly to ML models for immediate predictions
- Decoupled Architecture: Separate data collection, preprocessing, and model inference
- Load Balancing: Distribute heavy ML workloads across multiple workers
- Buffer Management: Handle traffic spikes without overwhelming your ML services

## Architecture
![overview-architecture](assets/overview-architecture.png)

## Common Use Cases in ML

### Real-time Model Serving Architecture

Real-time ML serving architecture where multiple clients can request predictions simultaneously while maintaining high throughput and low latency.

![realtime-serving](assets/stream-serving.png)

- Clients: Multiple users/systems sending prediction requests
- Request Queue: Manages incoming prediction requests
- ML Model Service: Consumes requests and generates predictions
- Results Queue: Stores predictions for client retrieval
- Results Database: Persistent storage for prediction history

### Model Pipeline Orchestration

```txt
[Raw Data] → RabbitMQ → [Preprocessing] → RabbitMQ → [Feature Engineering] → RabbitMQ → [Model Inference]
```

## Implementation Examples

### Example 1: Real-time Anomaly Detection

```python
# Consumer code snippet
def process_sensor_data(ch, method, properties, body):
    # Decode the message
    sensor_data = json.loads(body)
    
    # Apply ML model
    anomaly_score = anomaly_detection_model.predict(sensor_data)
    
    # Take action if anomaly detected
    if anomaly_score > THRESHOLD:
        alert_system.send_alert(sensor_data, anomaly_score)
```

### Example 2: Image Classification Pipeline

```python
# Producer code snippet
def send_image_batch(image_path):
    # Load and preprocess image
    image = preprocess_image(image_path)
    
    # Send to queue
    channel.basic_publish(
        exchange='',
        routing_key='image_classification_queue',
        body=image.tobytes(),
        properties=pika.BasicProperties(
            content_type='image/jpeg',
            headers={'image_size': image.shape}
        )
    )
```

## Setup and Run

### Running the Producer and Consumer within Docker Containers

#### Step 1: Build and Start the Services


Build and start the services using Docker Compose:

   ```shell
   docker compose -f docker-compose.yaml up -d
   ```

   This command will build the Docker images and start the RabbitMQ and producer services.

#### Step 2: Verify RabbitMQ

Access the RabbitMQ management UI to verify that RabbitMQ is running. Open your browser and go to:

   ```txt
   http://localhost:15672
   ```

   The default username and password are both `guest`.

#### Step 3: Run the Consumers

##### Run the CSV Consumer

1. Open a new terminal window.

2. Run the consumer script to start consuming messages from the RabbitMQ queue:

   ```shell
   python consumer/tabular_consumer.py --rabbitmq_server localhost --queue_name alicpp_records
   ```

   This script will start consuming messages from the specified RabbitMQ queue and print them to the console.

##### Run the Image Consumer

1. Open a new terminal window.

2. Run the image consumer script to start consuming image data from the RabbitMQ queue:

   ```shell
   python consumer/image_consumer.py --rabbitmq_server localhost --queue_name image_queue --output_directory received_images
   ```

   This script will start consuming image data from the specified RabbitMQ queue and save the images to the `received_images` directory.

##### Run the Text Consumer

1. Open a new terminal window.

2. Run the text consumer script to start consuming text data from the RabbitMQ queue:

   ```shell
   python consumer/text_consumer.py --rabbitmq_server localhost --queue_name text_queue --output_directory received_texts
   ```

   This script will start consuming text data from the specified RabbitMQ queue and save the words to the `received_texts` directory.

### Running the Producer Scripts Locally

#### Prerequisites

- Ensure RabbitMQ is running locally. You can start RabbitMQ using Docker (skip it if you have already run `docker-compose`):

  ```shell
  docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
  ```

- Install the necessary Python packages:

  ```shell
  pip install -r requirements-dev.txt
  ```

#### Run the Tabular Data Producer

1. Navigate to the `producer` directory.

2. Run the tabular data producer script:

   ```shell
   python stream_tabular_ingestion.py --mode setup --rabbitmq_server localhost
   ```

#### Run the Image Data Producer

1. Navigate to the `producer` directory.

2. Run the image data producer script:

   ```shell
   python stream_image_ingestion.py --directory images_data --rabbitmq_server localhost --queue_name image_queue
   ```

#### Run the Text Data Producer

1. Navigate to the `producer` directory.

2. Run the text data producer script:

   ```shell
   python stream_text_ingestion.py --directory texts_data --rabbitmq_server localhost --queue_name text_queue
   ```

## Notes

- The producer services will automatically start sending messages to the RabbitMQ queue once the services are up and running.
- The consumer scripts need to be run manually in separate terminal windows.

## Troubleshooting

- If you encounter any issues with the RabbitMQ connection, ensure that the RabbitMQ server is running and accessible.
- Check the logs of the Docker containers for any error messages:

  ```shell
  docker logs <container_name>
  ```
