from decouple import config
from config import LLAMA_MODEL,HUGGING_FACE_MODEL
from langchain_community.chat_models.huggingface import ChatHuggingFace
#from langchain_community.llms import HuggingFaceHub,HuggingFaceEndPoint
from langchain_community.llms import HuggingFaceHub,HuggingFaceEndpoint
from langchain_community.chat_models.ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
import os

os.environ['huggingfacehub_api_token'] = config('HUGGING_FACE_NEW_WRITE_TOKEN')

examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]

promptTemplate = ChatPromptTemplate.from_messages([
    ('human','{input}'),
    ('ai','{output}')
])

prompt = FewShotChatMessagePromptTemplate(examples=examples,example_prompt=promptTemplate)

messages = ChatPromptTemplate.from_messages([
    ('system','You are a wondrous wizard of math.'),
    prompt,
    ('human','{input}')
])

messages = messages.format_messages(input="What's the area square of a triangle?")


#################### Chat Ollama Model

model = ChatOllama(model=LLAMA_MODEL)
response = model.invoke(messages)
print("Chat Ollama Response:")
print(response.content)

#################### Hugging Face Endpoint

model = HuggingFaceEndpoint(repo_id=HUGGING_FACE_MODEL)
model = ChatHuggingFace(llm=model)

response = model.invoke(messages)
print('Chat Hugging Face Response: ')
print(response.content)