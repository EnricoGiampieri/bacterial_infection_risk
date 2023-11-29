
# streamlit run infection_risk.py
import streamlit as st
import pandas as pd
import numpy as np

st.title('Public health risk arising from the presence of Campylobacter spp. in the broiler meat chain')

x_low, x_top = st.sidebar.slider('_Campylobacter spp._ prevalence in broiler flocks sent to slaughter', 0.0, 1.0, (0.45, 0.55))
z_low, z_top = st.sidebar.slider('_Campylobacter spp._ concentration in broiler caeca content', 0.0, 3.0, (0.5, 1.0))

x_base = np.linspace(0, 7, 101)
y_base = x_base/(x_base+1)

v_low = x_low*z_low
v_top = x_top*z_top

v = x_base/(x_base+1)
v[x_base<v_low] = np.nan
v[x_base>v_top] = np.nan

x_label = 'average Campylobacter spp. bacterial load ( Log10 cfu/g)'

chart_data = pd.DataFrame({
    x_label: x_base,
    'risk function': y_base,
    'actual risk range': v,
})
st.line_chart(
    chart_data, 
    x=x_label, 
    y=["risk function", "actual risk range"],
    color=["#ff0000", "#007777"],

)





