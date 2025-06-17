import os
import getpass
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.llms import OpenAI
import streamlit as st
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
#llm 
open_ai_key = os.environ.get("OPENAI_API_KEY")
llm = OpenAI(temperature=0.8)

# UI
st.title("Langchain Demo")
input_text = st.text_input("What do you want to search?")

if input_text:
    try:
        st.write(llm(input_text))
    except AttributeError:
        print("Application failed")