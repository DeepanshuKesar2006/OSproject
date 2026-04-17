# dashboard.py

import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="ML OS Dashboard", layout="wide")

st.title("🚀 ML-Based Network Traffic Scheduler")
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, key="refresh")
st.markdown("### Real-time OS + Machine Learning Monitoring System")

LOG_FILE = "log.txt"

# AUTO REFRESH BUTTON
st.button("🔄 Refresh")

def load_data():
    if not os.path.exists(LOG_FILE):
        return pd.DataFrame(columns=["Length", "Protocol", "Type"])
    try:
        df = pd.read_csv(LOG_FILE, names=["Length", "Protocol", "Type"])
        return df
    except:
        return pd.DataFrame(columns=["Length", "Protocol", "Type"])

df = load_data()

# LAST UPDATED TIME
st.caption(f"Last Updated: {datetime.now().strftime('%H:%M:%S')}")

# METRICS
col1, col2, col3 = st.columns(3)

video_count = len(df[df["Type"] == "video"])
browsing_count = len(df[df["Type"] == "browsing"])
download_count = len(df[df["Type"] == "download"])

col1.metric("🎥 Video", video_count)
col2.metric("🌐 Browsing", browsing_count)
col3.metric("📥 Download", download_count)

st.divider()

# LAST DETECTED
st.subheader("⚡ Last Detected Traffic")
if not df.empty:
    st.success(df.tail(1).to_string(index=False))
else:
    st.warning("No data yet...")

st.divider()

# TABLE
st.subheader("📊 Live Data")
st.dataframe(df.tail(10), use_container_width=True)

st.divider()

# GRAPH
st.subheader("📈 Traffic Distribution")
if not df.empty:
    st.bar_chart(df["Type"].value_counts())
else:
    st.info("No data for graph")

st.divider()

# DOWNLOAD
st.download_button("⬇️ Download Logs", df.to_csv(index=False), "traffic_logs.csv")
