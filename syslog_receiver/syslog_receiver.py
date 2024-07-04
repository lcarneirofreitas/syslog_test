import socket
import time
from collections import defaultdict
from queue import Queue, Full
import threading

class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.timestamp = time.time()

    def consume(self, tokens=1):
        now = time.time()
        elapsed = now - self.timestamp
        self.timestamp = now
        self.tokens += elapsed * self.rate
        if self.tokens > self.capacity:
            self.tokens = self.capacity
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

# Setup UDP server to receive syslog messages
server_address = ('', 514)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

# Initialize token buckets for rate limiting
buckets = defaultdict(lambda: TokenBucket(rate=10, capacity=50))

# Setup a queue to store incoming messages
message_queue = Queue(maxsize=1000)  # Adjust the size as needed

message_counter = 0

def process_message(message, address):
    global message_counter
    ip = address[0]
    bucket = buckets[ip]
    if bucket.consume():
        message_counter += 1
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        print(f"{timestamp} - {message_counter} - Message from {ip}: {message.decode().strip()}")
    else:
        print(f"Message from {ip} dropped due to rate limit")

def handle_message():
    while True:
        try:
            message, address = message_queue.get(timeout=1)
            process_message(message, address)
        except Exception as e:
            continue

# Start a thread to handle messages from the queue
thread = threading.Thread(target=handle_message)
thread.start()

while True:
    data, address = sock.recvfrom(4096)
    try:
        message_queue.put_nowait((data, address))
    except Full:
        print(f"Message from {address[0]} dropped due to full queue")
