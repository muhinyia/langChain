from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import chromadb

load_dotenv()

GROQ_API_KEY = os.environ["GROQ_API_KEY"]

llm = ChatGroq(
    
    model_name="llama-3.3-70b-versatile", 
    temperature=1,
    groq_api_key = GROQ_API_KEY,
)

# response = llm.invoke("Who were the first men to walk on the moon?")

# print(response.content)
chroma_client = chromadb.Client()

collection = chroma_client.create_collection("authors")
collection.add(
    documents =[
        "Professor Ngugi wa Thiong'o is a reknown author",
        "Chimamanda Ngozi Adichie is really doing well in literature",
        "David Goggins is a great author",
        "Christopher Hitchens wrote great radical works",
        "Lumumba is a great author and Orator",
        "wole Soyinka won a nobel",
    ],
    ids = ["id1", "id2", "id3", "id4", "id5", "id6"]
)

results_1 = collection.query(query_texts=["This query is about Nigeria"], n_results=3)

print(results_1)

results_2 = collection.query(query_texts=["This query is about USA"], n_results=2)

print(results_2)