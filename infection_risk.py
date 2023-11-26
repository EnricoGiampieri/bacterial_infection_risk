
# streamlit run infection_risk.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Infection risk from food contamination model')

x_low, x_top = st.sidebar.slider('fraction of infected animals', 0.0, 1.0, (0.45, 0.55))
z_low, z_top = st.sidebar.slider('bacterial load per infected animal', 0.0, 3.0, (0.5, 1.0))

x_base = np.linspace(0, 5, 101)
y_base = x_base/(x_base+1)

v_range = np.linspace(x_low*z_low, x_top*z_top, 101)
v = v_range/(v_range+1)

chart_data = pd.DataFrame({
    'x': x_base,
    'y': y_base,
    'vb': v_range,
    'v': v,
})

fig, ax = plt.subplots()

ax.plot(chart_data["vb"], chart_data["v"], color="red", linewidth=2, label="actual risk range")
ax.plot(chart_data["x"], chart_data["y"], color="blue", linewidth=1, label="risk function")
ax.set_xlabel("average bacterial load")
ax.set_ylabel("human infection risk")
ax.axvspan(min(chart_data["vb"]), max(chart_data["vb"]), color="red", alpha=0.1)
ax.axhspan(min(chart_data["v"]), max(chart_data["v"]), color="red", alpha=0.1)
ax.legend()

st.pyplot(fig)

