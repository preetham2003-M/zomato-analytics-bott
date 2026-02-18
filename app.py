import streamlit as st
import pandas as pd
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Zomato AI Bot", layout="wide")

st.title("🤖 Zomato AI Analytics Assistant")
st.write("Ask anything about the dataset like ChatGPT.")

# Load dataset
df = pd.read_csv("Zomato Dataset.csv")

# Show dataset loaded
st.success("Dataset Loaded Successfully!")

# Create Hugging Face client
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=st.secrets["HUGGINGFACEHUB_API_TOKEN"]
)

# Chat history memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask your question here...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Create intelligent prompt
    prompt = f"""
You are a professional data analyst.

Here are the dataset columns:
{list(df.columns)}

Here are first 5 rows:
{df.head().to_string()}

User question:
{user_input}

Answer clearly in simple English.
If calculation is required, explain logically.
"""

    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.3
    )

    bot_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
