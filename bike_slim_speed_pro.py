
import streamlit as st
import numpy as np

# Constants
GRAVITY = 9.81
ROLLING_RESISTANCE = 0.004
AIR_DENSITY = 1.225
DRAG_COEFF = 0.63
FRONTAL_AREA = 0.5
BIKE_WEIGHT = 8

def calculate_speed(power, weight, gradient, distance_km):
    weight_total = weight + BIKE_WEIGHT
    slope_radians = np.arctan(gradient / 100)
    sin_theta = np.sin(slope_radians)
    cos_theta = np.cos(slope_radians)

    gravity_force = GRAVITY * weight_total * sin_theta
    rolling_resistance_force = GRAVITY * weight_total * ROLLING_RESISTANCE * cos_theta

    velocity = 5
    for _ in range(100):
        air_resistance = 0.5 * AIR_DENSITY * DRAG_COEFF * FRONTAL_AREA * velocity**2
        total_force = gravity_force + rolling_resistance_force + air_resistance
        velocity = power / total_force

    speed_kmh = velocity * 3.6
    time_hours = distance_km / speed_kmh
    return speed_kmh, time_hours * 60

st.set_page_config(page_title="Bike Slim Speed Pro", page_icon="🚴‍♂️", layout="centered")

st.title("🚴‍♂️ Bike Slim Speed Pro")
st.markdown("**See how much faster you'd ride by losing weight.**")
st.markdown("_Built for cyclists by PostiDeus_")

current_weight = st.number_input("Current weight (kg)", min_value=40.0, max_value=150.0, value=90.0)
goal_weight = st.number_input("Goal weight (kg)", min_value=40.0, max_value=150.0, value=82.0)
power_input = st.slider("Average Power (watts)", min_value=100, max_value=500, value=250)

gradient = st.slider("Gradient (%)", min_value=0.0, max_value=15.0, value=7.0)
distance_km = st.slider("Distance (km)", min_value=1.0, max_value=20.0, value=5.0)

speed_current, time_current = calculate_speed(power_input, current_weight, gradient, distance_km)
speed_goal, time_goal = calculate_speed(power_input, goal_weight, gradient, distance_km)

time_diff = time_current - time_goal
speed_diff = speed_goal - speed_current

st.markdown("### 📊 Results")
st.write(f"At **{current_weight}kg**, you'll complete the ride in **{time_current:.1f} minutes** at {speed_current:.1f} km/h.")
st.write(f"At **{goal_weight}kg**, you'll complete the ride in **{time_goal:.1f} minutes** at {speed_goal:.1f} km/h.")
st.markdown(f"**⏱️ Time saved:** `{time_diff:.1f}` minutes  
**⚡ Speed gain:** `{speed_diff:.1f}` km/h")

st.markdown("---")
st.markdown("🔥 **Want to actually drop that weight and ride faster?**")
st.markdown("[Join the Weight Loss Challenge →](https://www.trainwithus.cc/weightloss)  
[Join the Winter Training Group →](https://www.trainwithus.cc/wintergroup)")

st.markdown("---")
st.markdown("📂 **Optional: Upload your .fit file (coming soon)**")
uploaded_file = st.file_uploader("Upload your .fit file to auto-fill power", type=["fit"])

if uploaded_file:
    st.info("💡 FIT file parsing not yet implemented. In the final version, your average power will be auto-detected.")
