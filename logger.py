def log_data(length, proto, label):
    with open("log.txt", "a") as f:
        f.write(f"{length},{proto},{label}\n")
