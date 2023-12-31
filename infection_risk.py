
# streamlit run infection_risk.py
import streamlit as st
import pandas as pd
import numpy as np

st.title('Public health risk arising from the presence of _Campylobacter spp._ in the broiler meat chain')

x_low, x_top = st.sidebar.slider('_Campylobacter spp._ prevalence in broiler flocks sent to slaughter', 0, 100, (45, 55))
z_low, z_top = st.sidebar.slider('_Campylobacter spp._ concentration in broiler caeca content', 0.0, 7.0, (0.5, 1.0))
t_low, t_top = st.sidebar.slider('Probability of exposure to an infectious dose for the population of interest', 0, 100, (45, 55))

x_low /= 100.0
t_low /= 100.0

x_top /= 100.0
t_top /= 100.0

x_base = np.linspace(0, 7, 101)
y_base = x_base/(x_base+1)

v_low = x_low*z_low*t_low
v_top = x_top*z_top*t_top

v = x_base/(x_base+1)
v[x_base<v_low] = np.nan
v[x_base>v_top] = np.nan


st.write('### public health risk as a function of _Campylobacter spp._ concentration in broiler caeca content')
# if I put the dot after the name, it crashes the graphics...
x_label = "Campylobacter spp concentration (Log10 cfug/g)"
chart_data = pd.DataFrame({
    x_label: x_base,
    'risk function (%)': y_base*100,
    'actual risk range (%)': v*100,
})
st.line_chart(
    chart_data, 
    x=x_label, 
    y=["risk function (%)", "actual risk range (%)"],
    color=["#ff0000", "#003333"],
)

st.write(f'lower bound for the risk: {np.nanmin(v)*100:>3.2f}%')
st.write(f'upper bound for the risk: {np.nanmax(v)*100:>3.2f}%')

x_base = np.linspace(0, 1, 101)
y_base = x_base**3/(x_base**3+0.5**3)
v = y_base.copy()

v_low = x_low*t_low
v_top = x_top*t_top
v[x_base<v_low] = np.nan
v[x_base>v_top] = np.nan

st.write('### public health risk as a function of _Campylobacter spp._ prevalence in broiler flocks')
x_label = "Campylobacter spp prevalence"
chart_data = pd.DataFrame({
    x_label: x_base*100,
    'risk function (%)': y_base*100,
    'actual risk range (%)': v*100,
})
st.line_chart(
    chart_data, 
    x=x_label, 
    y=["risk function (%)", "actual risk range (%)"],
    color=["#ff0000", "#003333"],
)

st.write(f'lower bound for the risk: {np.nanmin(v)*100:>3.2f}%')
st.write(f'upper bound for the risk: {np.nanmax(v)*100:>3.2f}%')
