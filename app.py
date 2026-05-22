import streamlit as st
import pandas as pd
import plotly.express as px

st.title("2026 Tamil Nadu Election Analysis")

# Use the image data percentages for the chart
data = {
    'Party': ['TVK', 'DMK', 'ADMK', 'INC', 'PMK', 'Others'],
    'VoteShare': [34.92, 24.19, 21.21, 3.37, 1.20, 15.11]
}
df_plot = pd.DataFrame(data)

fig = px.pie(df_plot, values='VoteShare', names='Party', hole=0.5, title="2026 Party-Wise Vote Share")
st.plotly_chart(fig)