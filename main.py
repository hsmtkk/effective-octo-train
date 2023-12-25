import os

import dotenv
import streamlit as st
from openai import OpenAI

dotenv.load_dotenv()


def chat(prompt: str) -> str:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4",
    )
    return chat_completion.model_dump()["choices"][0]["message"]["content"]


st.header("OpenAI Chat with Streamlit")

prompt = st.text_input(label="Prompt")

if st.button(label="Submit"):
    response = chat(prompt)
    st.text(response)
