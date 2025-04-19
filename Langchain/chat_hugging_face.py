#from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.llms import HuggingFaceHub,HuggingFaceEndpoint
from langchain_core.messages import HumanMessage,SystemMessage
from config import HUGGING_FACE_MODEL
from decouple import config
import os

os.environ['huggingfacehub_api_token']=config('HUGGING_FACE_NEW_WRITE_TOKEN')
#llm = HuggingFaceHub(repo_id=HUGGING_FACE_MODEL)
llm = HuggingFaceEndpoint(repo_id=HUGGING_FACE_MODEL,task="conversational")
model = ChatHuggingFace(llm = llm)
print(model)
messages = [SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="What is the purpose of model regularization?")]

response = model.invoke(messages)
print(response)