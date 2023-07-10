import streamlit as st
import pandas as pd

st.title("Hello ereryone")

st.header("This is a streamlit header")

df = pd.read_csv("https://storage.googleapis.com/cloud-boot-app-bucket/1553768847-housing.csv")

st.dataframe(df) #table o dataframe

st.subheader()
selected_option=st.selectbox(
    "Seleziona opzione:"
    ["Opzione 1", "Opzione 2"]
)
st.write(selected_option)
selected_options=st.multiselect(
    "Seleziona opzione:"
    ["Opzione 1", "Opzione 2"]
)
st.write(selected_options)