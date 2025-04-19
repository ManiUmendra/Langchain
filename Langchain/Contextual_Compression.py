from langchain_ollama import ChatOllama
from langchain_ollama.embeddings import OllamaEmbeddings
from config import LLAMA_MODEL
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_community.document_loaders import TextLoader
from langchain_experimental.text_splitter import SemanticChunker


llm = ChatOllama(model=LLAMA_MODEL)
embeddings = OllamaEmbeddings(model=LLAMA_MODEL)
text_loader = TextLoader(".\\science.txt")
text = text_loader.load()
print("load")
chunk = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=50)
doc = chunk.split_documents(text)
print("Length of Doc:",len(doc))

vector_stores = FAISS.from_documents(documents=doc,embedding=embeddings)
vector_stores.save_local('semantic_science')
print("vector saved")
#retriever = FAISS.load_local('chro_db',OllamaEmbeddings(model=LLAMA_MODEL),allow_dangerous_deserialization=True).as_retriever()

compressor = LLMChainExtractor.from_llm(llm=llm)
retriever = vector_stores.as_retriever()

compression_retriever = ContextualCompressionRetriever(base_compressor=compressor,base_retriever=retriever)
text_1 = "What are the three major branches of modern science?"
result = compression_retriever.invoke(text_1)
print(result)

