# Packet Capture and Logging with PyShark

This script captures network packets on a specified interface and logs the details, including timestamp, source and destination IP addresses, source and destination ports, and the transport protocol (TCP/UDP). It runs for 60 seconds and logs the information to both a console and a log file (`packet_info.log`).

## Requirements

- Python installed on your machine.
- **PyShark** library, which is a wrapper around the Wireshark command-line tools. Install it using `pip install pyshark`.
- Root/Administrator permissions to capture packets on network interfaces (required for packet sniffing).
- Basic knowledge of networking and protocols (e.g., TCP, UDP, IP).

## How to Use

### 1. Install Dependencies

Install the **PyShark** library by running the following command:

pip install pyshark

### 2. Change Network Interface

In the script, change the network interface to the one you want to capture packets from. By default, it is set to `eth0` (Ethernet). You may need to update this to your own network interface (e.g., `wlan0` for wireless networks).

capture = pyshark.LiveCapture(interface='eth0')  # Change 'eth0' to your interface

### 3. Run the Script

Once everything is set up, run the script:

sudo python capture_ips_ports.py

This will start capturing packets for 60 seconds, log the details to `packet_info.log`, and print the details to the console.

### 4. Check the Log File

After the capture, the script will generate a log file named `packet_info.log`. You can open it to review the captured packet details:

cat packet_info.log

## Example Output

In both the log file (`packet_info.log`) and the cli, the captured packet details will be written in the following format:

[2024-11-24 13:30:08] Source IP: 192.168.1.5 -> Destination IP: 8.8.8.8, Source Port: 12345 -> Destination Port: 53, Protocol: UDP

[2024-11-24 13:30:09] Source IP: 192.168.1.7 -> Destination IP: 8.8.8.8, Source Port: 54321 -> Destination Port: 443, Protocol: TCP

These details will also be printed in real-time to the console during packet capture.

## Notes

- **Permissions**: Root or administrator permissions are required to capture packets from network interfaces.
- **Network Interface**: Make sure to set the correct network interface (eth0, wlan0, etc.) based on your machine's configuration.
- **Security**: Be mindful of any sensitive data captured during network sniffing. Use this script responsibly.
- **Performance**: The script captures packets for 60 seconds by default. You can modify the timeout value in the script to capture for a different duration if needed.

## License

This project is open-source under the MIT License.
