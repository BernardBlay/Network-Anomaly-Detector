import scapy.all as scapy
import statistics
from colorama import Fore, Style

# Define a threshold to detect anomalous packet sizes
THRESHOLD = 2.0

# List to store packet sizes for analysis
packet_sizes = []

# Function to capture packets
def packet_callback(packet):
    if packet.haslayer(scapy.IP):  # Check if the packet contains an IP layer
        packet_size = len(packet)  # Get the size of the packet
        src_ip = packet[scapy.IP].src  # Get the source IP address
        packet_sizes.append((packet_size, src_ip))  # Add packet size and source IP to the list

        # Only analyze traffic after capturing at least 2 packets
        if len(packet_sizes) > 1:
            analyze_traffic()

# Function to detect anomalies using Z-score (simple calculation)
def analyze_traffic():
    sizes = [size for size, _ in packet_sizes]
    mean = statistics.mean(sizes)
    std_dev = statistics.stdev(sizes)

    if std_dev > 0:  # Ensure standard deviation is not zero
        last_packet_size, last_src_ip = packet_sizes[-1]
        z_score = (last_packet_size - mean) / std_dev

        # Check if the Z-score exceeds the threshold
        if abs(z_score) > THRESHOLD:
            print(f"{Fore.RED}Anomalous packet detected!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Source IP: {last_src_ip}{Style.RESET_ALL}")
            print(f"Size: {last_packet_size} bytes, Z-score: {z_score:.2f}")
            print(f"{Fore.RED}Reason:{Style.RESET_ALL} This packet size deviates from the average packet size by {abs(z_score):.2f} standard deviations.")
            
            # Explanation for why it's flagged
            if z_score > 0:
                print(f"The packet is much larger than average, indicating unusually large traffic.\n")
            else:
                print(f"The packet is much smaller than average, indicating unusually small traffic.\n")
        else:
            print(f"{Fore.GREEN}Normal packet from {last_src_ip}{Style.RESET_ALL}")
            print(f"Size: {last_packet_size} bytes, Z-score: {z_score:.2f}\n")
    else:
        print(f"{Fore.BLUE}Not enough variation in packet sizes yet.{Style.RESET_ALL}")

# Start sniffing live traffic (no count or timeout to keep it running continuously)
print(f"{Fore.CYAN}Sniffing network traffic... Press Ctrl+C to stop.{Style.RESET_ALL}")
scapy.sniff(prn=packet_callback)
