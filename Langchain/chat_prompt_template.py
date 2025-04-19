from langchain_core.prompts import ChatPromptTemplate
#from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.chat_models import ChatOllama
from config import LLAMA_MODEL, HUGGING_FACE_MODEL, HUGGING_FACE_NEW_WRITE_TOKEN
import os

os.environ['huggingfacehub_api_token'] = HUGGING_FACE_NEW_WRITE_TOKEN

messages = [
     ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
]

promptTemplate = ChatPromptTemplate.from_messages(messages)
prompt = promptTemplate.format_messages(name="Umendra",user_input="What is your name?")

#####  Ollama Chat Model

model = ChatOllama(model=LLAMA_MODEL)
response = model.invoke(prompt)

print("Chat Ollama Output :::::::::::::::::::")
print(response.content)


##### Chat HuggingFace Model
llm = HuggingFaceEndpoint(repo_id=HUGGING_FACE_MODEL)
model = ChatHuggingFace(llm=llm)
response = model.invoke(prompt)

print("Chat HuggingFace Output :::::::::::::::::::")
print(response.content)