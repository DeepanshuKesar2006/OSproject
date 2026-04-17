import matplotlib.pyplot as plt
import csv

video = browsing = download = 0

with open("log.txt", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] == "video":
            video += 1
        elif row[2] == "browsing":
            browsing += 1
        else:
            download += 1

labels = ["Video", "Browsing", "Download"]
values = [video, browsing, download]

plt.bar(labels, values)
plt.title("Traffic Classification Result")
plt.show()
