import streamlit as st
import time
import pickle
import os
from helper import load_csv, vector_convertion, get_chain


st.title("CSV File Uploader and Query Interface")
st.sidebar.title("Upload a CSV file")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])
process_url_clicked = st.sidebar.button("Convert")
temp_file_path = "temp_uploaded_file.csv"
vec_file_path = "vector_index.pkl"

def save_uploaded_file(uploadedfile):
    with open(temp_file_path, "wb") as f:
        f.write(uploadedfile.getbuffer())
    st.sidebar.success(f"{uploadedfile.name} saved successfully!")

main_placeholder = st.empty()

if process_url_clicked:
    # save the file
    save_uploaded_file(uploaded_file)
    # load the file
    data =load_csv(temp_file_path)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    
    # convert to vector
    vector_index = vector_convertion(data)
    main_placeholder.text("vector convertion ...Started...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(vec_file_path, "wb") as f:
        pickle.dump(vector_index, f)

    
query = main_placeholder.text_input("Question: ")

if query:
    if os.path.exists(vec_file_path):
        with open(vec_file_path, "rb") as f:
            vector_index = pickle.load(f)
           
        # built the chain
        chain = get_chain(vector_index)        
        output = chain(query)
        
        # result will be a dictionary of this format --> {"answer": "", "sources": [] }
        st.header("Answer")
        st.write(output["result"])