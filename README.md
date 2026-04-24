ML-Based OS-Level Network Scheduling using Linux Traffic Control (tc)
Overview

This project implements an intelligent operating system-level network scheduler that combines Machine Learning with Linux Traffic Control (tc) to dynamically prioritize network traffic.

The system captures live packets, classifies them into traffic categories using a trained Random Forest classifier, and automatically applies QoS bandwidth scheduling policies at the Linux kernel level using HTB (Hierarchical Token Bucket).

It demonstrates how machine learning can enhance traditional operating system scheduling mechanisms through adaptive, data-driven resource management.

Features
Live packet capture using Scapy
Packet classification using Machine Learning
Dynamic QoS scheduling using Linux tc
HTB-based bandwidth shaping
Traffic logging and monitoring
Jupyter notebook simulation version
Ubuntu kernel-enforced implementation
Traffic Classes

The classifier categorizes packets into:

Video Traffic → High Priority (5 Mbps)
Web Browsing → Medium Priority (2 Mbps)
File Download → Low Priority (1 Mbps)
System Architecture
Live Traffic
   ↓
Packet Capture (Scapy)
   ↓
Feature Extraction
(Packet Length + Protocol)
   ↓
Random Forest Classifier
   ↓
Traffic Prediction
   ↓
Linux tc + HTB Scheduler
   ↓
Dynamic QoS Enforcement
Technologies Used
Python
Scapy
Scikit-learn
Joblib
Pandas
Matplotlib
Linux Traffic Control (tc)
Ubuntu 22.04
Project Structure
.
├── main.py
├── capture.py
├── features.py
├── classify.py
├── scheduler.py
├── model.pkl
├── log.txt
├── notebook/
│   └── ML_os_jupyter.ipynb
└── report/
    └── Project_Report.pdf
Machine Learning Model

Model used:

Random Forest Classifier
100 Estimators
Features:
Packet Length
Protocol Number

Traffic classes:

Video
Browsing
Download
Linux Traffic Control Configuration

Example setup:

sudo tc qdisc add dev enp0s8 root handle 1: htb default 3

sudo tc class add dev enp0s8 parent 1: classid 1:1 htb rate 5mbit
sudo tc class add dev enp0s8 parent 1: classid 1:2 htb rate 2mbit
sudo tc class add dev enp0s8 parent 1:3 htb rate 1mbit

Run the Project
Jupyter Notebook Version
jupyter notebook

Run all notebook cells.

Ubuntu Kernel Version

Run as root:

sudo python3 main.py

Check interface:

ip addr

Verify tc statistics:

tc -s qdisc show dev enp0s8
Sample Output
Packet Length: 1514
Protocol: 6
Detected: video

QoS Applied: video -> 5mbit
Results
Real-time packet classification
Adaptive bandwidth prioritization
Kernel-level QoS enforcement
~96% classification accuracy (experimental)
Applications
Smart Routers
QoS Traffic Management
Campus/Enterprise Networks
Datacenter Scheduling
SDN and Edge Networking Research
Future Work
Deep Learning Traffic Classification
Reinforcement Learning Scheduling
Per-flow tc Filters
eBPF Integration
Research Contribution

This project explores a novel intersection of:

Operating Systems
Machine Learning
Network Scheduling

by embedding learned decision-making into kernel-level resource management.
