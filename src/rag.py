print("rag.py started")

from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQAWithSourcesChain

load_dotenv()
import os
print("GROQ_API_KEY found:", bool(os.getenv("GROQ_API_KEY")))

# constants
CHUNK_SIZE = 1000
EMBEDDING_MODEL_NAME = "Alibaba-NLP/gte-base-en-v1.5"
VECTORSTORE_DIR = Path(__file__).parent / "src/vectorstore/vectorstore"
COLLECTION_NAME = "real-estate-assistant"

# global components
llm = None
vectore_store = None

def initialize_components():
    global llm, vectore_store
    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.9, max_tokens=500)

    if vectore_store is None:
        vectore_store = Chroma(
        embedding_function=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME, model_kwargs={"trust_remote_code": True}),
        persist_directory=str(VECTORSTORE_DIR),
        collection_name=COLLECTION_NAME,
        )


def process_urls(urls):

    print("initializing components...")
    initialize_components()

    vectore_store.reset_collection()

    print("Load data...")
    loader = WebBaseLoader(urls)
    data = loader.load()

    print("Split text...")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=CHUNK_SIZE,
    )
    docs = text_splitter.split_documents(data)

    print("Adding documents to vector store...")
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vectore_store.add_documents(docs, ids=uuids)


def generate_answer(query):
    if not vectore_store:
        raise RuntimeError("Vector store is not initialized")

    # Fixed the variable assignment here to be cleaner
    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm,
        retriever=vectore_store.as_retriever()
    )

    result = chain.invoke({"question": query}, return_only_outputs=True)
    return result.get("answer", ""), result.get("sources", "")


if __name__ == "__main__":
    urls = [
        "https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
        "https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html"
    ]
    process_urls(urls)
    answer, sources = generate_answer("What was the 30 year fixed mortgage rate along with the date?")
    print(f"Answer: {answer}")
    print(f"Sources: {sources}")
