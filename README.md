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



## 🔐 Disclaimer

This tool is intended for educational and ethical use only. Do not use it on networks without explicit authorization.

## 👨🏾‍💻 Author

Bernard Blay  
Cybersecurity Enthusiast  
Ghana  
bernardblay123@gmail.com

## 🏷️ Topics
cybersecurity • network-security • python • anomaly-detection • packet-sniffing • scapy • z-score
