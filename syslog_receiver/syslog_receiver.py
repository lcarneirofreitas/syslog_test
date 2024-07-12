import sys
import socket

# Setup UDP server to receive syslog messages
server_address = ('syslog-receiver', 514)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)


while True:
    data, address = sock.recvfrom(4096)
    ip = address[0]
    print(f"{data.decode().strip()}")
    sys.stdout.flush()  # Flush stdout to ensure logs are written immediately
