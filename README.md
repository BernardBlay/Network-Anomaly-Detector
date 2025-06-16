# Network-Anomaly-Detector
# 🧠 How It Works
1. Captures packets using Scapy’s `sniff()` function
2. Extracts packet size and source IP
3. Calculates mean and standard deviation of packet sizes
4. Computes Z-score for the latest packet
5. Flags anomalous packets if Z-score > 2.0

Anomalies typically represent either extremely large or small packets, which can indicate network scanning, DoS attacks, or other suspicious activities.

# 📁 Project Files
| File                   | Description                                 |
|------------------------|---------------------------------------------|
| `Anomaly_Detection.py` | Main Python script for packet analysis      |
| `requirements.txt`     | Python libraries needed to run the project  |
| `.gitignore`           | Hides temporary and system files            |
| `LICENSE`              | MIT license for open use                    |
| `README.md`            | Project documentation                       |



##Installation Guide
To run this project, first clone the repository using git clone https://github.com/YOUR_USERNAME/network-anomaly-detector.git and then navigate into the folder using cd network-anomaly-detector. After that, install the required Python libraries by running pip install scapy colorama. You don’t need to install statistics because it’s already included in Python by default. Once everything is installed, start the program using sudo python Anomaly_Detection.py. This will begin sniffing live packets on your network and will flag any anomalies based on packet size using Z-score calculations. The required dependencies are scapy and colorama



## 🔐 Disclaimer

This tool is intended for educational and ethical use only. Do not use it on networks without explicit authorization.

## 👨🏾‍💻 Author

Bernard Blay  
Cybersecurity Enthusiast  
Ghana  
bernardblay123@gmail.com

## 🏷️ Topics
cybersecurity • network-security • python • anomaly-detection • packet-sniffing • scapy • z-score
