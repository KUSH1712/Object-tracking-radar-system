


import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

st.set_page_config(layout="wide")
st.title("Object tracking radar system")

DATA_FILE = "radar_data.csv"
REFRESH_RATE = 2  # in seconds
MAX_RANGE_CM = 100
BEAM_TRAIL_LENGTH = 5  # How many previous angles to show as sweep trail

# Load and trim latest data
try:
    df = pd.read_csv(DATA_FILE)
except:
    st.warning("Waiting for sensor data...")
    st.stop()

df = df.tail(50)  # Keep recent entries only

# Setup session state
if "angle_history" not in st.session_state:
    st.session_state.angle_history = []

# Unique sorted angles
angle_list = sorted(df["angle"].unique())
if not angle_list:
    st.warning("No angle data yet.")
    st.stop()

# Update current sweep angle index
if "sweep_index" not in st.session_state:
    st.session_state.sweep_index = 0

current_angle = angle_list[st.session_state.sweep_index]
st.session_state.angle_history.append(current_angle)

# Limit beam trail
if len(st.session_state.angle_history) > BEAM_TRAIL_LENGTH:
    st.session_state.angle_history = st.session_state.angle_history[-BEAM_TRAIL_LENGTH:]

# Object tracking logic (repeat detections at same angle & distance ~±5cm)
tracked_objects = []
angle_distance_pairs = {}

for _, row in df.iterrows():
    key = (row["angle"] // 10 * 10)  # angle bucket
    distance_bucket = round(row["distance"] / 5) * 5

    if (key, distance_bucket) in angle_distance_pairs:
        angle_distance_pairs[(key, distance_bucket)] += 1
    else:
        angle_distance_pairs[(key, distance_bucket)] = 1

    if angle_distance_pairs[(key, distance_bucket)] >= 2:
        tracked_objects.append((row["angle"], row["distance"]))

# ---- Plot Radar ----
fig = go.Figure()

# Plot sweep trail (fading lines)
for i, angle in enumerate(reversed(st.session_state.angle_history)):
    opacity = 1.0 - (i / BEAM_TRAIL_LENGTH)
    fig.add_trace(go.Scatterpolar(
        r=[0, MAX_RANGE_CM],
        theta=[angle, angle],
        mode='lines',
        line=dict(color='lime', width=2),
        opacity=opacity,
        showlegend=False
    ))

# Plot detected objects (dots)
fig.add_trace(go.Scatterpolar(
    r=df["distance"],
    theta=df["angle"],
    mode='markers',
    marker=dict(color='red', size=10),
    name='Objects'
))

# Plot tracked objects (larger blue dots)
if tracked_objects:
    r_vals = [d for _, d in tracked_objects]
    theta_vals = [a for a, _ in tracked_objects]
    fig.add_trace(go.Scatterpolar(
        r=r_vals,
        theta=theta_vals,
        mode='markers',
        marker=dict(color='blue', size=14, symbol='circle-open-dot'),
        name='Tracked Objects'
    ))

# Layout
fig.update_layout(
    polar=dict(
        radialaxis=dict(range=[0, MAX_RANGE_CM], visible=True),
        angularaxis=dict(direction="clockwise", rotation=90)
    ),
    showlegend=True,
    height=650,
    margin=dict(l=10, r=10, t=30, b=10)
)

st.plotly_chart(fig, use_container_width=True)

# Step forward in sweep
st.session_state.sweep_index = (st.session_state.sweep_index + 1) % len(angle_list)

# Refresh
time.sleep(REFRESH_RATE)
st.experimental_rerun()
