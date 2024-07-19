# Project Name

This project is a simple test that simulates using Envoy as a UDP connection proxy for syslog servers, which are simulated using Python.

The components of this stack are:

1. The client sends a UDP syslog message to the Envoy proxy.
2. The Envoy proxy receives the messages and forwards them through load balancers to two downstreams, which are our syslog servers.
3. The syslog servers receive the messages and display them in the output logs.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Installation

Instructions to install the project locally. Can include terminal commands:

```bash
git clone https://github.com/lcarneirofreitas/syslog_test
cd syslog_test
```

## Usage

Examples of how to use the project after installation.

Running the stack with docker compose:

```bash
docker compose up --build -d
```

In another terminal, you can view the Envoy proxy statistics:

```bash
while true; do
  clear
  curl -s http://127.0.0.1:10001/stats | egrep 'syslog|udp' | grep -v "\: 0"
  sleep 1
done
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Project Link: https://github.com/lcarneirofreitas/syslog_test





