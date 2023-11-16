import streamlit as st
import numpy as np

def calculate_dimensions(dielectric_constant, h, f):
    # Speed of light
    c = 3 * 10**8  # in m/s
    # Convert height to meters
    h = h * 10**-3
    # Convert frequency to Hz
    f = f * 10**9
    # Initial guess for width (W)
    W = c / (2 * f * np.sqrt((dielectric_constant + 1) / 2))
    # Calculate effective dielectric constant
    e_eff = (dielectric_constant + 1) / 2 + (dielectric_constant - 1) / 2 * (1 / np.sqrt(1 + 12 * (h / W)))
    # Adjust W with the new effective dielectric constant
    W = c / (2 * f * np.sqrt(e_eff))
    # Calculate L
    L = c / (2 * f * np.sqrt(e_eff)) - 0.824 * h * (np.sqrt((e_eff + 0.3) * (W/h + 0.264) / (e_eff - 0.258) * (W/h + 0.8)))
    # Convert meters to mm
    W = W * 10**3
    L = L * 10**3
    return W, L

st.title('Optimistation of Antenna Design')
st.header('Using Machine Learning Techniques to Optimise Antenna Design')
st.caption('Shiv Nadar University - Electrical Engineering Major Project')
st.sidebar.write('List of Contents')
st.sidebar.button('Microstrip Patch Antenna Calculator')

st.sidebar.button('Antenna Design and Dataset')
st.sidebar.button('Training Model')
st.sidebar.button('Comparison and Mean percentage errors')
st.sidebar.button('Sandbox')

col1, col2 = st.columns(2)
with col1:
    st.subheader('Microstrip Antenna Dimension Calculator')
    st.image('antenna.png', width=200)

with col2:
    dielectric_constant = st.number_input('Dielectric Constant', min_value=1.0, value=4.4, step=0.1)
    dielectric_height = st.number_input('Dielectric Height (mm)', min_value=0.1, value=1.6, step=0.1)
    frequency = st.number_input('Operation Frequency (GHz)', min_value=0.1, value=2.4, step=0.1)

if st.button('Calculate'):
    width, length = calculate_dimensions(dielectric_constant, dielectric_height, frequency)
    st.write(f'Width: {width:.2f} mm')
    st.write(f'Length: {length:.2f} mm')

st.divider()

st.subheader('Antenna Design and Dataset')
st.divider()
st.subheader('Training Model')
st.divider()
st.subheader('Comparison and Mean percentage errors')
st.divider()
st.subheader('Sandbox')
st.divider()
