# classify.py

import random

def classify_packet(length, proto):
    # Realistic + dynamic behavior

    if proto == 6:  # TCP
        if length > 1000:
            return "video"
        elif length > 300:
            return "download"
        else:
            return random.choice(["browsing", "browsing", "download"])

    elif proto == 17:  # UDP (YouTube, streaming often UDP)
        return random.choice(["video", "video", "browsing"])

    else:
        return "browsing"
