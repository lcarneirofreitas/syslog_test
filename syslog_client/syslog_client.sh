#!/bin/bash

server="envoy-proxy"
port=10000

message_counter=0

# Função para gerar mensagem aleatória
generate_random_message() {
    words=("error" "info" "warning" "debug" "critical")
    details=("disk full" "network down" "file not found" "CPU load high" "memory leak detected")
    word=${words[$RANDOM % ${#words[@]} ]}
    detail=${details[$RANDOM % ${#details[@]} ]}
    echo "${word}: ${detail}"
}

# Loop infinito para enviar mensagens
while true; do
    ((message_counter++))
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    random_message=$(generate_random_message)
    message="Counter: ${message_counter}      Message: ${random_message}"
    echo -n "$message" | nc -u -w1 "$server" "$port"
    echo "$message"
    #sleep 1  # Ajuste o tempo de espera conforme necessário
done
