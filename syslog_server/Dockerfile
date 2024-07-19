# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install iproute2 and tzdata package to use tc command and set timezone
RUN apt-get update && apt-get install -y iproute2 tzdata

# Copy the Python script and entrypoint script into the container
COPY syslog_server.py /app/syslog_server.py
COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
