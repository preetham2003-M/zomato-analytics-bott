import streamlit as st
import pandas as pd
from huggingface_hub import InferenceClient

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Zomato AI Analytics Assistant")

st.title("Zomato AI Analytics Assistant")
st.write("Ask anything about the dataset. The AI will analyze and answer.")

# -------------------------
# LOAD DATASET
# -------------------------
try:
    df = pd.read_csv("Zomato.csv")   # Make sure file name matches exactly
    st.success("Dataset Loaded Successfully!")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# -------------------------
# LOAD HUGGING FACE MODEL
# -------------------------
HF_TOKEN = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN,
)

# -------------------------
# USER INPUT
# -------------------------
question = st.text_input("Ask your question:")

if question:

    # Create dataset context
    dataset_preview = df.head(20).to_string()

    prompt = f"""
You are a data analytics assistant.

Here is a preview of the dataset:

{dataset_preview}

Answer this question clearly and professionally:

{question}
"""

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
        )

        answer = response.choices[0].message.content

        st.markdown("### Answer:")
        st.write(answer)

    except Exception as e:
        st.error(f"Error generating response: {e}")
