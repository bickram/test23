import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Fruits List")

# -----Create a Dictionary & DataFrame--------
_dic = {'Name': ['Mango', 'Apple', 'Banana'], 'Quantity': [45, 38, 90]}
_df = pd.DataFrame(_dic)
# Create a button
load = st.button('Load Data')

if "load_state" not in st.session_state:
    st.session_state.load_state = False
if load or st.session_state.load_state:
    st.session_state.load_state = True
    st.write(_df)
    # User option
    opt = st.radio('Plot type:', ['Bar', 'Pie'])
    if opt == 'Bar':
        fig = px.bar(_df, x='Name', y='Quantity', title='Bar Chart')
        st.plotly_chart(fig)
    else:
        fig = px.pie(_df, names='Name', values='Quantity', title='Pie Chart')
        st.plotly_chart(fig)
