#!/bin/bash

# Apply tc commands for rate limiting
#tc qdisc add dev eth0 root handle 1: htb default 30
#tc class add dev eth0 parent 1: classid 1:1 htb rate 1mbit
#tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip dport 514 0xffff flowid 1:1

# Start the Python syslog receiver script
exec python /app/syslog_receiver.py
