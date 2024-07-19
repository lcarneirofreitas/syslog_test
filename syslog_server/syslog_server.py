import sys
import socket
import threading

def syslog_server(port):
    server_address = ('', port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    
    print(f"Syslog server listening on port {port}")
    
    while True:
        data, address = sock.recvfrom(4096)
        ip = address[0]
        print(f"{data.decode().strip()}")
        sys.stdout.flush()  # Flush stdout to ensure logs are written immediately

# Create and start threads for each port
ports = [514, 515]
threads = []

for port in ports:
    thread = threading.Thread(target=syslog_server, args=(port,))
    threads.append(thread)
    thread.start()

# Join threads to the main thread
for thread in threads:
    thread.join()
