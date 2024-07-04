import sys
import socket

# Setup UDP server to receive syslog messages
server_address = ('', 514)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

message_counter = 0

while True:
    data, address = sock.recvfrom(4096)
    ip = address[0]
    message_counter += 1
    print(f"Message {message_counter} from {ip}: {data.decode().strip()}")
    sys.stdout.flush()  # Flush stdout to ensure logs are written immediately
