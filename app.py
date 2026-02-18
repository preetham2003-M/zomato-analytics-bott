import streamlit as st
import pandas as pd

st.title("Zomato Delivery Analytics Bot")

# Load dataset
df = pd.read_csv("Zomato.csv")

st.success("Dataset Loaded Successfully!")

# Show actual column names (very important)
st.write("Available Columns:")
st.write(df.columns)

query = st.text_input("Ask a question about the dataset:")

if query:
    q = query.lower()

    # Top rows
    if "top" in q or "first" in q:
        st.write(df.head())

    # Columns
    elif "column" in q:
        st.write(df.columns)

    # Shape
    elif "shape" in q:
        st.write("Dataset Shape:", df.shape)

    # Describe
    elif "describe" in q or "summary" in q:
        st.write(df.describe())

    # Lowest value (automatic numeric detection)
    elif "lowest" in q:
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            col = numeric_cols[0]
            st.write(f"Lowest value in {col}:", df[col].min())
        else:
            st.write("No numeric columns found.")

    # Highest value
    elif "highest" in q:
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            col = numeric_cols[0]
            st.write(f"Highest value in {col}:", df[col].max())
        else:
            st.write("No numeric columns found.")

    # Average
    elif "average" in q:
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            col = numeric_cols[0]
            st.write(f"Average value of {col}:", df[col].mean())
        else:
            st.write("No numeric columns found.")

    else:
        st.write("Sorry, I cannot answer that question yet.")
