# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install tzdata package to set timezone
RUN apt-get update && apt-get install -y tzdata

# Set the timezone to America/Sao_Paulo
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy the Python script into the container
COPY syslog_client.py /app/syslog_client.py

# Run the Python script
CMD ["python", "/app/syslog_client.py"]
