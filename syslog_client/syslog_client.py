import socket
import time
import sys

# Server address and port
server_address = ('syslog-receiver', 514)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message_counter = 0

# Function to send syslog messages
def send_syslog_message(message):
    sock.sendto(message.encode(), server_address)
    print(f"Sent: {message}")
    sys.stdout.flush()  # Flush stdout to ensure logs are written immediately

# Continuously send syslog messages
while True:
    message_counter += 1
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    message = f'<134>1 {timestamp} {message_counter} - - - - Test syslog message'
    send_syslog_message(message)
    #time.sleep(0.5)  # Adjust the sleep time to control the rate of messages
