stats = {
    "video": 0,
    "browsing": 0,
    "download": 0
}

def update_stats(label):
    if label in stats:
        stats[label] += 1

def print_stats():
    print("📊 Stats:", stats)
