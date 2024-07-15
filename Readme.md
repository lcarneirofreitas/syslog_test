docker compose up --build -d

while true; do
  clear
  curl -s http://127.0.0.1:10001/stats | egrep 'syslog|udp' | grep -v "\: 0"
  sleep 1
done
