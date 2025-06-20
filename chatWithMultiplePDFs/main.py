import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings,HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        
        for page in pdf_reader.pages:
            text += page.extract_text()
            
    return text
        
def get_chunks(raw_text):
    textSplitter = CharacterTextSplitter(separator="`\n", 
                                         chunk_size=1000,
                                         chunk_overlap=200,
                                         length_function=len)
    
    chunks = textSplitter.split_text(text=raw_text)
    return chunks

def get_vector_store(text_chunks):
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name='hkunlp/instructor-large')
    vectorStore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)    
    return vectorStore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat history", 
                                      return_messages=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
                                                                llm=llm, 
                                                               retriever=vectorstore.as_retriever(), 
                                                               memory=memory)
    return conversation_chain

def main():
    load_dotenv()
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
        
    st.set_page_config(page_title="Chat with Multiple PDF files", page_icon=":books:")
    st.header("Chat with multiple PDFS :books:")
    st.text_input("Ask something about your documents:")
    
    with st.sidebar:
        st.subheader("Your documents:")
        pdf_docs = st.file_uploader("upload your PDFs here and then click 'Process' button", accept_multiple_files=True, type="pdf")
        
        if st.button("Process"):
            with st.spinner("Proccessing"):
                # get pdf files
                raw_text = get_pdf_text(pdf_docs=pdf_docs)
                                
                # chunk text
                
                text_chunks = get_chunks(raw_text=raw_text)
                
                # st.write(len(chunks))
            
                # vectorize the chunks
                vectorStore = get_vector_store(text_chunks)
                
                # get conversation
                st.session_state.conversation = get_conversation_chain(vectorstore=vectorStore)
                
                st.write(st.session_state.conversation)
                
                

if __name__ == "__main__":
    
    main()