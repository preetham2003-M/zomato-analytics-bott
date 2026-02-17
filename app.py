import streamlit as st
import pandas as pd

st.title("Zomato Delivery Analytics Bot")

# Load dataset
df = pd.read_csv("Zomato.csv")

st.success("Dataset Loaded Successfully!")

query = st.text_input("Ask a question about the dataset:")

if query:

    q = query.lower()

    # 1. Top rows
    if "top" in q or "first" in q:
        st.write(df.head())

    # 2. Columns
    elif "column" in q:
        st.write(df.columns)

    # 3. Shape
    elif "shape" in q:
        st.write("Dataset Shape (Rows, Columns):")
        st.write(df.shape)

    # 4. Total restaurants
    elif "total restaurants" in q:
        st.write("Total Restaurants:", len(df))

    # 5. Average rating
    elif "average rating" in q:
        st.write("Average Rating:", df["rate"].mean())

    # 6. Highest rating
    elif "highest rating" in q:
        st.write("Highest Rating:", df["rate"].max())

    # 7. Lowest rating
    elif "lowest rating" in q:
        st.write("Lowest Rating:", df["rate"].min())

    # 8. Restaurants per city
    elif "restaurants per city" in q:
        st.write(df["location"].value_counts())

    # 9. Online delivery count
    elif "online delivery" in q:
        st.write(df["online_order"].value_counts())

    # 10. Table booking count
    elif "table booking" in q:
        st.write(df["book_table"].value_counts())

    # 11. Average cost
    elif "average cost" in q:
        st.write("Average Cost for Two:", df["approx_cost(for two people)"].mean())

    # 12. Describe dataset
    elif "describe" in q or "summary" in q:
        st.write(df.describe())

    else:
        st.write("Sorry, I cannot answer that question yet.")
