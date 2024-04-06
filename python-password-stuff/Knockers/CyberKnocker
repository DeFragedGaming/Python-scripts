import nmap
import subprocess

def knock_ports(target_ip, port_range):
    try:
        subprocess.run(['hydra', '-q', '-s', port_range, '-L', 'usernames.txt', '-P', 'passwords.txt', '-o', 'hydra.log', '-t', '4', '-f', '-v', target_ip, 'ftp', 'ssh', 'telnet'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing Hydra:", e)

def scan_ports(target_ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip, arguments='-p 1-65535 -T4 -v')
    
    open_ports = []
    for host in nm.all_hosts():
        port_info = nm[host]['tcp']
        for port in port_info:
            if port_info[port]['state'] == 'open':
                open_ports.append(port)
                
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the target IP address to scan for open ports: ")
    port_range = input("Enter the port range to knock (e.g., 21-23): ")
    
    open_ports = scan_ports(target_ip)
    
    if open_ports:
        print("Open ports found on", target_ip, ": ", open_ports)
        
        services = input("Enter services to target (comma-separated, e.g., ftp,ssh,telnet): ").split(',')
        
        print("Knocking ports...")
        knock_ports(target_ip, port_range)
    else:
        print("No open ports found on", target_ip)
