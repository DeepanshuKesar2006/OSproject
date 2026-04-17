# scheduler.py

import os

def setup_tc():
    print("⚙️ Setting up Traffic Control...")
    os.system("sudo tc qdisc del dev enp0s8 root 2>/dev/null")
    os.system("sudo tc qdisc add dev enp0s8 root handle 1: htb")

def apply_qos(label):
    if label == "video":
        rate = "5mbit"
    elif label == "download":
        rate = "2mbit"
    else:
        rate = "1mbit"

    print(f"🚦 Applying QoS: {label} → {rate}")
