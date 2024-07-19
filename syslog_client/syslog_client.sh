#!/bin/bash

message_counter=0

generate_random_message() {
    words=("error" "info" "warning" "debug" "critical")
    details=("disk full" "network down" "file not found" "CPU load high" "memory leak detected")
    word=${words[$RANDOM % ${#words[@]} ]}
    detail=${details[$RANDOM % ${#details[@]} ]}
    echo "${word}: ${detail}"
}

while true; do
    ((message_counter++))
    random_message=$(generate_random_message)
    message="Counter: ${message_counter}      Message: ${random_message}"
    echo -n "$message" | nc -u -w1 "$ENVOY_SERVER" "$ENVOY_PORT"
    echo "$message"
    sleep "${SLEEP_TIMEOUT:-1}"
done
