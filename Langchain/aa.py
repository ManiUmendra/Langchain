# from config import HUGGING_FACE_TOKEN,HUGGING_FACE,HUGGING_FACE_NEW_WRITE_TOKEN,HUGGING_FACE_1_RESTRICTED

# from transformers import AutoTokenizer, AutoModel
# import torch,os

# os.environ['token'] = HUGGING_FACE_NEW_WRITE_TOKEN

# # Load the LLaMA model and tokenizer
# model_name = HUGGING_FACE_1_RESTRICTED  # Replace with the actual model name, e.g., "facebook/llama-7b"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModel.from_pretrained(model_name)
# print(model)


from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from config import LLAMA_MODEL
from langchain_ollama import ChatOllama, OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
#from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor


####################  Character Splitter
llm = OllamaLLM(model=LLAMA_MODEL)
embeddings = OllamaEmbeddings(model=LLAMA_MODEL)

# text = TextLoader(".\\science.txt").load()

# split_text = CharacterTextSplitter(separator=' ',chunk_size=500,chunk_overlap=0)
# doc = split_text.split_documents(text)
# print("done")
# vector = FAISS.from_documents(documents=doc,embedding=embeddings)
# vector.save_local('character_split')

vector = FAISS.load_local(".//character_split",embeddings=embeddings,allow_dangerous_deserialization=True)
retriever = vector.as_retriever()

compressor = LLMChainExtractor.from_llm(llm=llm)

contextual_compressor = ContextualCompressionRetriever(base_compressor=compressor,base_retriever=retriever)
print("done")
question = "What are the three major branches of modern science?"
result = contextual_compressor.invoke(question)
print(result)
