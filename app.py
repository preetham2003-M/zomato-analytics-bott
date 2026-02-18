import streamlit as st
import pandas as pd

st.set_page_config(page_title="Zomato Analytics Bot", layout="wide")

st.title("🍽️ Zomato Delivery Analytics Bot")
st.markdown("Ask intelligent questions about the dataset.")

# Load Dataset
try:
    df = pd.read_csv("Zomato.csv")
    st.success("Dataset Loaded Successfully!")
except:
    st.error("Dataset not found. Please check file name.")
    st.stop()

query = st.text_input("Ask a question about the dataset:")

if query:
    q = query.lower()

    # ---------------- BASIC INFO ----------------
    if "top" in q or "first" in q:
        st.subheader("Top 5 Rows")
        st.dataframe(df.head())

    elif "columns" in q:
        st.subheader("Column Names")
        st.dataframe(pd.DataFrame(df.columns, columns=["Columns"]))

    elif "shape" in q:
        st.subheader("Dataset Shape")
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

    elif "describe" in q or "summary" in q:
        st.subheader("Statistical Summary")
        st.dataframe(df.describe())

    # ---------------- NUMERIC ANALYSIS ----------------
    elif "lowest" in q:
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            col = numeric_cols[0]
            st.write(f"Lowest value in {col}:", df[col].min())
        else:
            st.write("No numeric columns found.")

    elif "highest" in q:
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            col = numeric_cols[0]
            st.write(f"Highest value in {col}:", df[col].max())
        else:
            st.write("No numeric columns found.")

    elif "average" in q or "mean" in q:
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            col = numeric_cols[0]
            st.write(f"Average value of {col}:", round(df[col].mean(),2))
        else:
            st.write("No numeric columns found.")

    # ---------------- SPECIFIC COLUMN INTELLIGENCE ----------------
    elif "rating" in q:
        if "Delivery_person_Ratings" in df.columns:
            st.write("Average Rating:", round(df["Delivery_person_Ratings"].mean(),2))
            st.write("Highest Rating:", df["Delivery_person_Ratings"].max())
            st.write("Lowest Rating:", df["Delivery_person_Ratings"].min())
        else:
            st.write("Rating column not found.")

    elif "age" in q:
        if "Delivery_person_Age" in df.columns:
            st.write("Average Age:", round(df["Delivery_person_Age"].mean(),2))
            st.write("Minimum Age:", df["Delivery_person_Age"].min())
            st.write("Maximum Age:", df["Delivery_person_Age"].max())
        else:
            st.write("Age column not found.")

    # ---------------- DEFAULT ----------------
    else:
        st.warning("I cannot answer that question yet. Try asking about top rows, columns, shape, rating, age, average, lowest, highest etc.")
