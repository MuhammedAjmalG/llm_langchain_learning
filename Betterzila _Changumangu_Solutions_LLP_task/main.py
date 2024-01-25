##initialize our streamlit app
import streamlit as st
import time
import pickle
from helper import *

st.set_page_config(page_title="Q&A Demo")
st.header("Google palm LLM Q&A Application on Custom Data")
# side bar section
pdf = st.sidebar.file_uploader("Upload a PDF file", type="pdf")
generate = st.sidebar.button("Process Pdf")

# function to save uploaded file
temp_file_path = "temp_uploaded_file.pdf"
def save_uploaded_file(pdf):
    with open(temp_file_path, "wb") as f:
        f.write(pdf.getbuffer())
    st.sidebar.success(f"{pdf.name} saved successfully!")

file_path = "vector_index_file.pkl"
main_placeholder = st.empty()

if generate and pdf is not None:
    # load data
    save_uploaded_file(pdf)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = get_content_pdf(temp_file_path)
    
    # split data
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = convert_to_chunks(data)

    # create embeddings and save it to FAISS index
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    vectorstore = vector_convertion(docs)
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

query=st.text_input("Enter a Query regarding your pdf : ",key="query")
submit=st.button("Generate Response")

if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            
if submit and query is not None:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
    chain=chain_function(vectorstore)
    response = chain(query)

    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", query))
    st.subheader("The Response is")

    st.write(response['result'])
    st.subheader("The source is")
    st.write(response['source_documents'][0].metadata['source'])

    st.session_state['chat_history'].append(("Bot", response['result']))

# Display chat history in the sidebar

st.sidebar.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.sidebar.write(f"{role}: {text}")