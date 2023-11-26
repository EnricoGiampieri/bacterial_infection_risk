
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

v_low = x_low*z_low
v_top = x_top*z_top

v = x_base/(x_base+1)
v[x_base<v_low] = np.nan
v[x_base>v_top] = np.nan

chart_data = pd.DataFrame({
    'average bacterial load': x_base,
    'risk function': y_base,
    'actual risk range': v,
})
st.line_chart(chart_data, x="average bacterial load", y=["risk function", "actual risk range"], color=["#ff0000", "#00ffff"])
#fig, ax = plt.subplots()

#ax.plot(chart_data["vb"], chart_data["v"], color="red", linewidth=2, label="actual risk range")
#ax.plot(chart_data["x"], chart_data["y"], color="blue", linewidth=1, label="risk function")
#ax.set_xlabel("average bacterial load")
#ax.set_ylabel("human infection risk")
#ax.axvspan(min(chart_data["vb"]), max(chart_data["vb"]), color="red", alpha=0.1)
#ax.axhspan(min(chart_data["v"]), max(chart_data["v"]), color="red", alpha=0.1)
#ax.legend()

#st.pyplot(fig)

