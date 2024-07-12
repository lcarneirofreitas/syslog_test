import socket
import time
import sys
import random

# Server address and port
server_address = ('envoy-proxy', 10000)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message_counter = 0

# Function to send syslog messages
def send_syslog_message(message):
    sock.sendto(message.encode(), server_address)
    print(f"{message}")
    sys.stdout.flush()  # Flush stdout to ensure logs are written immediately

# Example random message generator
def generate_random_message():
    words = ["error", "info", "warning", "debug", "critical"]
    details = ["disk full", "network down", "file not found", "CPU load high", "memory leak detected"]
    return f"{random.choice(words)}: {random.choice(details)}"

# Continuously send syslog messages
while True:
    message_counter += 1
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    random_message = generate_random_message()
    message = f'Counter: {message_counter}      Message: {random_message}'
    send_syslog_message(message)
    time.sleep(1)  # Adjust the sleep time to control the rate of messages
