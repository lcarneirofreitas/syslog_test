# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install iproute2 and tzdata package to use tc command and set timezone
RUN apt-get update && apt-get install -y iproute2 tzdata

# Set the timezone to America/Sao_Paulo
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy the Python script and entrypoint script into the container
COPY syslog_receiver.py /app/syslog_receiver.py
COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose the syslog UDP port
EXPOSE 514/udp

# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
