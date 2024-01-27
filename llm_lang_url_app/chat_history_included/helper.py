# libraries imported
import os
from dotenv import load_dotenv 
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

#load the keys
load_dotenv()

# load data from url
def load_data_from_url(url):

    loaders = UnstructuredURLLoader(urls=url)
    data = loaders.load()
    return data

url=(["https://learnenglish-new.com/english-stories-to-improve-english/"])

# split into chunks
def covert_to_chunks(data):
    spliter = RecursiveCharacterTextSplitter(
        separators=["\n\n","\n","."],
        chunk_size = 400,
        chunk_overlap = 80)
    docs  = spliter.split_documents(data)
    return docs

#lets convert the junk to vectors and store to vector database
def vector_convertion(docs):
    embed = HuggingFaceInferenceAPIEmbeddings(
    api_key=os.getenv('HUG_API_KEY'),
    model_name="sentence-transformers/all-MiniLM-l6-v2")
    vectorindex = FAISS.from_documents(docs, embed)
    return vectorindex

#now lets buit the prompt and chain
def chain_function(vectorindex):
    model = GooglePalm(google_api_key=os.getenv('API_KEY'),temperature=0.1, max_tokens=200)
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""


    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}
    chain = RetrievalQA.from_chain_type(llm=model,
                                chain_type="stuff",
                                retriever=vectorindex.as_retriever(score_threshold = 0.7),
                                input_key="query",
                                return_source_documents=True,
                                chain_type_kwargs=chain_type_kwargs)
    return chain




if __name__ == "__main__":
    data = load_data_from_url(url)
    docs = covert_to_chunks(data)
    vectorindex = vector_convertion(docs)
    chain = chain_function(vectorindex)
    response = chain("how many chapters are there in this story?")
    print(response['result'])
