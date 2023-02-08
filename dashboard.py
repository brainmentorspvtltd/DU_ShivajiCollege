import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('ipldata_19/matches.csv')

st.set_page_config(
    page_title='IPL Dashboard',
    layout='wide')

st.title("IPL Dashboard...")

filter = st.selectbox("Select the season", pd.unique(df['season']))
df = df[df['season'] == filter]

fig_1, fig_2 = st.columns(2)

with fig_1:
    st.markdown("Number of wins...")
    fig = px.bar(df['winner'])
    st.write(fig)

with fig_2:
    st.markdown("Number of matches in each venue...")
    fig = px.bar(df['venue'])
    st.write(fig)

fig_1, fig_2 = st.columns(2)

with fig_1:
    values = pd.value_counts(df['toss_decision'])
    fig = px.pie(df['toss_decision'], values=values, names=['field','bat'])
    st.write(fig)

with fig_2:
    st.markdown("Number of matchesin each season")
    fig = px.bar(df['venue'])
    st.write(fig)

st.dataframe(df)




