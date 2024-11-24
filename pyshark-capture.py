
import pyshark

# Open the log file to write IPs, ports, and protocols
log_file = open("packet_info.log", "a")

# Capture packets on the default network interface **change interface to desired one**
capture = pyshark.LiveCapture(interface='eth0')

# Start capturing packets (let it run for 60 seconds)
capture.sniff(timeout=60)

# Loop through the captured packets
for packet in capture:
    try:
        # Check if the packet has an IP layer
        if 'IP' in packet:
            source_ip = packet.ip.src
            dest_ip = packet.ip.dst

            # Check if the packet has a transport layer (TCP/UDP) for ports
            if 'TCP' in packet:
                source_port = packet.tcp.srcport
                dest_port = packet.tcp.dstport
                protocol = 'TCP'
            elif 'UDP' in packet:
                source_port = packet.udp.srcport
                dest_port = packet.udp.dstport
                protocol = 'UDP'
            else:
                source_port = 'N/A'
                dest_port = 'N/A'
                protocol = 'Other'

            # Write the details (IP, ports, and protocol) to the log file
            log_file.write(f"Source IP: {source_ip} -> Destination IP: {dest_ip}, "
                           f"Source Port: {source_port} -> Destination Port: {dest_port}, "
                           f"Protocol: {protocol}\n")

            # Print out the same information to the console
            print(f"Source IP: {source_ip} -> Destination IP: {dest_ip}, "
                  f"Source Port: {source_port} -> Destination Port: {dest_port}, "
                  f"Protocol: {protocol}")
    except AttributeError:
        # Ignore packets that don't have the expected layers ** ex.arp **
        pass

# Close the log file after capturing
log_file.close()