Packet Capture and Logging with PyShark

This script captures network packets on a specified interface and logs the details, including source and destination IP addresses, source and destination ports, and the transport protocol (TCP/UDP). It runs for 60 seconds and logs the information to both a console and a log file (packet_info.log).
What’s Inside:

    Captures live network packets on the specified network interface.
    Logs IP addresses, ports, and protocols (TCP/UDP) from the captured packets.
    Exports the captured data into a log file for later analysis.
    Prints out packet details in real-time to the console.

What You’ll Need:

    Python installed on your machine.
    PyShark library, which is a wrapper around the Wireshark command-line tools (Install with pip install pyshark).
    Root/Administrator permissions to capture packets on network interfaces.
    Basic knowledge of networking and protocols (e.g., TCP, UDP, IP).

Getting Started:

    Install PyShark: If you haven’t installed PyShark yet, you can do so by running:

    Change Network Interface: In the script, change the network interface to the one you want to capture packets from (e.g., 'eth0' or 'wlan0').

    Run the Script: Once everything is set up, simply run the script. It will capture packets for 60 seconds, then log the packet details to packet_info.log and print them to the console.

    Check the Log File: After the capture, open the packet_info.log file to review the captured packet details.

Example Output:

Log File (packet_info.log):

Source IP: 192.168.1.5 -> Destination IP: 8.8.8.8, Source Port: 12345 -> Destination Port: 53, Protocol: UDP

The script automatically writes to a log file and closes the file once the capture is complete. No manual cleanup is necessary.