from dotenv import load_dotenv
import os
import streamlit as st
from agents.tenk_agent import summarize_tenk, ask_about_tenk
from agents.tenq_agent import summarize_tenq, ask_about_tenq

# Load the .env file explicitly
load_dotenv()

# Check if SEC_API_KEY is loaded
SEC_API_KEY = os.getenv("SEC_API_KEY")
if not SEC_API_KEY:
    raise ValueError("SEC_API_KEY is missing! Check your .env file.")

st.title("AI-Powered Financial Chatbot")
st.subheader("Ask AI about 10-K and 10-Q filings!")

# Document type selection
doc_type = st.selectbox("Select Document Type:", ["10-K Report", "10-Q Report"])
ticker = st.text_input("Enter a stock ticker (e.g., AAPL):")
question = st.text_input("Ask a specific question about the filing:")

if st.button("Get Answer"):
    try:
        if doc_type == "10-K Report":
            if question:
                answer = ask_about_tenk(ticker, question)
                st.subheader("AI Response:")
                st.json(answer)
            else:
                summary = summarize_tenk(ticker)
                st.subheader("Filing Summary:")
                st.json(summary)
        elif doc_type == "10-Q Report":
            if question:
                answer = ask_about_tenq(ticker, question)
                st.subheader("AI Response:")
                st.json(answer)
            else:
                summary = summarize_tenq(ticker)
                st.subheader("Filing Summary:")
                st.json(summary)
    except Exception as e:
        st.error(str(e))
