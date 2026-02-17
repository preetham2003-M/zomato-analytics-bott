import streamlit as st
import pandas as pd

st.title("Zomato Delivery Analytics Bot")

# Load dataset
df = pd.read_csv("Zomato.csv")

st.write("Dataset Loaded Successfully!")

query = st.text_input("Ask a question about the dataset:")

if query:
    if "top" in query.lower():
        st.write(df.head())

    elif "columns" in query.lower():
        st.write(df.columns)

    elif "shape" in query.lower():
        st.write(df.shape)

    elif "describe" in query.lower():
        st.write(df.describe())

    else:
        st.write("Currently supports: top rows, columns, shape, describe.")
