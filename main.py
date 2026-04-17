# main.py

from scapy.all import sniff, IP
from classify import classify_packet
from scheduler import setup_tc, apply_qos
from logger import log_data
from stats import update_stats, print_stats

# Setup traffic control
setup_tc()

def process(packet):
    try:
        if packet.haslayer(IP):
            length = len(packet)
            proto = packet[IP].proto

            # ML classification
            label = classify_packet(length, proto)

            print(f"\n📦 Packet Length: {length}, Protocol: {proto}")
            print(f"🔍 Detected: {label}")

            # Apply OS-level scheduling
            apply_qos(label)

            # Logging + stats
            log_data(length, proto, label)
            update_stats(label)
            print_stats()

    except Exception as e:
        print("Error:", e)

print("🚀 Starting Live Packet Capture... Press CTRL+C to stop")

sniff(
    iface="enp0s8",   # ⚠️ change if needed
    prn=process,
    store=False
)
