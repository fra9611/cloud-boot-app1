import streamlit as st
import pandas as pd

st.title("Hello ereryone")

st.header("This is a streamlit header")

df = pd.read_csv("https://storage.googleapis.com/cloud-boot-app-bucket/1553768847-housing.csv")

st.table(df) #table o dataframe
