from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import LLAMA_MODEL
from langchain_ollama import ChatOllama, OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
#from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS


model = OllamaLLM(model=LLAMA_MODEL)
embeddings = OllamaEmbeddings(model=LLAMA_MODEL)
############################## Science Loader

text_loader = TextLoader(".\\science.txt")
text_1 = text_loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=300,chunk_overlap=10)
doc = text_splitter.split_documents(text_1)
print(type(doc))

# embed = embeddings.embed_documents(doc)
# print(len(doc))

vector = FAISS.from_documents(documents=doc,embedding=embeddings)
vector.save_local('faiss_index')

# print(type(vector))

# new_vector = FAISS.load_local('faiss_index',embeddings=embeddings)
new_vector=FAISS.load_local("chro_db",embeddings=embeddings,allow_dangerous_deserialization=True)
text_1 = "What ancient mesopotamians have studied for divinatory purposes?"
embed = embeddings.embed_query(text_1)
text_2 = "How does the concept of the rich get richer apply to areas like fame and knowledge?"
result = new_vector.similarity_search_by_vector(embed)
print(result)


# #text = "Give the name of important dieties of Hinduism."
# text = "What ancient mesopotamians studied for divinatory purposes?"
# result = vector.similarity_search(text) 
# # result = vector.similarity_search_by_vector(text)
# print(result)