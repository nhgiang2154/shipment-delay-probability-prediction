FROM python:3.9-slim

# Copy app handler code
COPY producer/stream_tabular_ingestion.py stream_tabular_ingestion.py
COPY producer/tabular_data.csv tabular_data.csv

# Install dependencies
RUN pip3 install pandas==2.2.3
RUN pip3 install pika==1.3.2

# This Dockerfile command runs a Python script named 'stream_tabular_ingestion.py'
# -u: Runs the Python interpreter in unbuffered mode. The script is executed with the 'setup' mode and connects
# to a RabbitMQ server named 'rabbitmq'.
CMD [ "python", "-u", "stream_tabular_ingestion.py", "--mode", "setup", "--rabbitmq_server", "rabbitmq"]