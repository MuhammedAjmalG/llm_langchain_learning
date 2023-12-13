import streamlit as st
import time
import pickle
import os
from helper import load_data_from_url, covert_to_chunks,vector_convertion,chain_function

st.title("Query Regarding any Content: 📈")
st.sidebar.title("Enter the source URL")
urls = []
for i in range(2):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_hug.pkl"
main_placeholder = st.empty()

if process_url_clicked:
    # load data
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = load_data_from_url(urls)
    
    # split data
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = covert_to_chunks(data)

    # create embeddings and save it to FAISS index
    vectorstore = vector_convertion(docs)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = chain_function(vectorstore)
            output = chain(query)
            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.write(output["result"])

            # Display sources, if available
            st.write(output['source_documents'][0].metadata['source'])
            
