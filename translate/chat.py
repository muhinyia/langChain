import getpass
import os
from langchain.chat_models import init_chat_model
from openai import OpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
# get the API Key
# if not os.environ.get("OPENAI_API_KEY"):
#     os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter the OpenAI API Key: ")
    
    
# model = init_chat_model("gpt-4o-mini", model_provider="openai")

# model.invoke("Hey Chat")


# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     input="Write a paragraph outlining the works of Prof. Ngugi wa Thiong'o."
# )

# print(response.output_text)

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter the OpenAI API Key: ")

model = init_chat_model("gpt-4o-mini", model_provider="openai")

messages = [
    SystemMessage("Translate the following from English into Gikuyu"),
    HumanMessage("Rest in Peace prof. Ngugi wa Thing'o! Indeed you are a legend!")
] 

response = model.invoke(messages)

print(response.content)

# chat
