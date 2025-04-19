from langchain_ollama import OllamaEmbeddings
from config import LLAMA_MODEL

model = OllamaEmbeddings(model="llama3.2:latest")


###################### Embed Documents
embedding = model.embed_documents([
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ])

print("For Embedding Documents ::::::::::::::::::::::")
for e in range(0,len(embedding)):
    print(len(embedding[e]))

####################### Embed Query

print("For Embed Query ::::::::::::::::::::::::")
embeddings = model.embed_query("What was the name mentioned in the conversation?")

print(len(embeddings))