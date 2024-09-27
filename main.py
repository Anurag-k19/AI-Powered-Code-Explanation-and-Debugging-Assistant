import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

load_dotenv()

#Enter your groq_api_key here
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

st.markdown("<h1 style='text-align: center;'>Code Explanation and Debugging Assistant</h1>", unsafe_allow_html=True)

user_input = st.text_area("Enter your code snippet or prompt here:", height=300)

if st.button("Explain Code"):
    if user_input:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": f"Explain the following code:\n\n{user_input}\n\nExplanation:"}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        st.subheader("Explanation:")
        response_text = ""
        for chunk in completion:
            response_text += chunk.choices[0].delta.content or ""
        st.write(response_text)
    else:
        st.warning("Please enter a code snippet or prompt.")

if st.button("Debug Code"):
    if user_input:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": f"Identify bugs in the following code and suggest fixes:\n\n{user_input}\n\nBugs and Fixes:"}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        st.subheader("Debugging Suggestions:")
        response_text = ""
        for chunk in completion:
            response_text += chunk.choices[0].delta.content or ""
        st.write(response_text)
    else:
        st.warning("Please enter a code snippet or prompt.")
