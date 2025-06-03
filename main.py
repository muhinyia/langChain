import pandas as pd
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.document import Document
from langchain.prompts import PromptTemplate
from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
import textwrap
import dotenv


transcriptions = pd.read_csv("data/mtsamples.csv")

# print(transcriptions["medical_specialty"])

cardio = transcriptions.loc[transcriptions["medical_specialty"] == "Cardiovascular / Pulmonary", :]
# cardio.reset_index(inplace=True)
print(cardio)