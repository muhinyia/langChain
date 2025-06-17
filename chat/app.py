from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helfpul assistant.Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)


# UI
st.title("Langcahin with OPENAI")
input_text = st.text_input("What do you want to search?")

# llm

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

# output

if input_text:
    st.write(chain.invoke({"question":input_text}))