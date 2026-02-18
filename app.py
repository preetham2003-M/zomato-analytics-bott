import streamlit as st
import pandas as pd
import openai
import os

st.set_page_config(page_title="Zomato AI Analytics Bot", layout="wide")

st.title("🤖 Zomato AI Analytics Bot")
st.markdown("Ask anything about the dataset. AI will analyze it.")

# ---- SET YOUR OPENAI API KEY ----
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ---- LOAD DATA ----
try:
    df = pd.read_csv("Zomato.csv")
    st.success("Dataset Loaded Successfully!")
except:
    st.error("Dataset file not found.")
    st.stop()

question = st.text_input("Ask your question:")

if question:
    
    prompt = f"""
    You are a data analyst.
    The dataframe is called df.
    The columns are: {list(df.columns)}.
    
    Write ONLY python pandas code to answer this question:
    {question}
    
    Return only code, no explanation.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    code = response.choices[0].message["content"]

    st.code(code)

    try:
        result = eval(code)
        st.write("### Result:")
        st.write(result)
    except Exception as e:
        st.error("Error executing AI generated code")
        st.write(e)
