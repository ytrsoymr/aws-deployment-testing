import streamlit as st
import requests

st.title("Calculator App")

a = st.number_input("Enter first number", value=0.0)
b = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Select operation", ["add", "subtract", "multiply", "divide"])

if st.button("Calculate"):
    url = f"http://127.0.0.1:8000/{operation}?a={a}&b={b}"
    try:
        response = requests.get(url)
        data = response.json()
        st.write(data)
    except Exception as e:
        st.error(f"Error: {e}")

