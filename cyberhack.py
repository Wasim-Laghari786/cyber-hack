import socket

def scan_ports(target_ip, port_range):
    """
    Scans the specified range of ports on a target IP address.
    """
    print(f"Scanning ports on {target_ip}...")
    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)  # Timeout for connection attempts
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)

    return open_ports


def main():
    print("Welcome to PortScanLite!")
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port (e.g., 1): "))
    end_port = int(input("Enter the ending port (e.g., 1000): "))
    
    open_ports = scan_ports(target_ip, (start_port, end_port))

    if open_ports:
        print(f"\n[RESULT] Open ports on {target_ip}: {open_ports}")
    else:
        print(f"\n[INFO] No open ports found in the specified range.")

if __name__ == "__main__":
    main()