# -*- coding: utf-8 -*-
"""Copy of Financial Bot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dcpQxF3do3VRxe7i39lm5n3IE5FqPX9i
"""

!pip install streamlit PyPDF2 langchain faiss-cpu openai

!pip install -U langchain-community

import streamlit as st
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import tempfile

def main():
    st.title("Financial Data Query System")
    st.markdown("Upload P&L PDFs and ask financial questions!")

    # File Upload Section
    uploaded_file = st.file_uploader("Upload a PDF file containing P&L data", type=["pdf"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            file_path = tmp_file.name

        # Process and extract data from PDF
        st.info("Processing uploaded PDF...")
        raw_text = extract_text_from_pdf(file_path)

        if raw_text:
            st.success("PDF processed successfully!")

            # Generate Embeddings
            st.info("Generating embeddings...")
            documents = preprocess_text(raw_text)
            vector_db = create_vector_store(documents)
            st.success("Embeddings generated and stored!")

            # Query Section
            user_query = st.text_input("Enter your financial query:")
            if user_query:
                st.info("Fetching answer...")
                answer, context = query_financial_data(vector_db, user_query)
                st.write(f"**Answer:** {answer}")
                st.write("**Relevant Context:**")
                st.write(context)
        else:
            st.error("Failed to extract text from the uploaded PDF.")

def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

def preprocess_text(raw_text):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(raw_text)
    documents = [Document(page_content=chunk) for chunk in chunks]
    return documents

def create_vector_store(documents):
    embeddings = OpenAIEmbeddings()  # Requires OpenAI API Key
    vector_db = FAISS.from_documents(documents, embeddings)
    return vector_db

def query_financial_data(vector_db, query):
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(model="text-davinci-003"), retriever=retriever, return_source_documents=True
    )
    response = qa_chain(query)
    answer = response["result"]
    context = "\n\n".join([doc.page_content for doc in response["source_documents"]])
    return answer, context

if __name__ == "__main__":
    main()

!pip install streamlit pyngrok
!pip install pyngrok

with open("financial_query_app.py.py", "w") as f:
    f.write("""!pip install streamlit PyPDF2 langchain faiss-cpu openai
    !pip install -U langchain-community
    import streamlit as st
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import tempfile
def main():
    st.title("Financial Data Query System")
    st.markdown("Upload P&L PDFs and ask financial questions!")

    # File Upload Section
    uploaded_file = st.file_uploader("Upload a PDF file containing P&L data", type=["pdf"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            file_path = tmp_file.name

        # Process and extract data from PDF
        st.info("Processing uploaded PDF...")
        raw_text = extract_text_from_pdf(file_path)

        if raw_text:
            st.success("PDF processed successfully!")

            # Generate Embeddings
            st.info("Generating embeddings...")
            documents = preprocess_text(raw_text)
            vector_db = create_vector_store(documents)
            st.success("Embeddings generated and stored!")

            # Query Section
            user_query = st.text_input("Enter your financial query:")
            if user_query:
                st.info("Fetching answer...")
                answer, context = query_financial_data(vector_db, user_query)
                st.write(f"**Answer:** {answer}")
                st.write("**Relevant Context:**")
                st.write(context)
        else:
            st.error("Failed to extract text from the uploaded PDF.")
            def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None
        def preprocess_text(raw_text):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(raw_text)
    documents = [Document(page_content=chunk) for chunk in chunks]
    return documents
    def create_vector_store(documents):
    embeddings = OpenAIEmbeddings()  # Requires OpenAI API Key
    vector_db = FAISS.from_documents(documents, embeddings)
    return vector_db
    def query_financial_data(vector_db, query):
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(model="text-davinci-003"), retriever=retriever, return_source_documents=True
    )
    response = qa_chain(query)
    answer = response["result"]
    context = "\n\n".join([doc.page_content for doc in response["source_documents"]])
    return answer, context

if __name__ == "__main__":
    main()""")

!npm install -g localtunnel

!streamlit run financial_query_app.py.py & npx localtunnel --port 8501

import os
os.environ["OPENAI_API_KEY"] = "your-api-key"

uploaded_file = st.file_uploader("Upload a PDF file containing P&L data", type=["pdf"])

!streamlit run financial_query_app.py.py & npx localtunnel --port 8501

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

user_query = st.text_input("Enter your financial query:")