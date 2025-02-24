import socket
from datetime import datetime

# fonction to scan the port -----------------
def scan_port(host, port):
    try:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except socket.error :
        print(f"Couldn't connect to {host}")

# ----------scan group of ports at the same time ---------
def scan_ports(host, start_port, end_port):
    print(f"Scanning host {host} from port {start_port} to {end_port}")
    start_time = datetime.now()
    
    # start_port --------> end_port
    for port in range(start_port, end_port + 1):
        scan_port(host, port)
        
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scan completed in {total_time}")

# -----------use the host ip ------------
host = "192.168.1.103"   
start_port = 20
end_port = 254

scan_ports(host, start_port, end_port)
