from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_community.llms import HuggingFaceEndpoint
from config import LLAMA_MODEL, HUGGING_FACE_MODEL, HUGGING_FACE_NEW_WRITE_TOKEN
import os

os.environ['huggingfacehub_api_token'] = HUGGING_FACE_NEW_WRITE_TOKEN

messages = "Tell me a {adjective} joke about {content}."
promptTemplate = PromptTemplate.from_template(messages)
prompt = promptTemplate.format(adjective="joke",content="man")

######### Ollama Model

llm = OllamaLLM(model=LLAMA_MODEL)
response = llm.invoke(prompt)

print("Ollama Response ::::::::")
print(response)


######### HuggingFace Model

llm = HuggingFaceEndpoint(repo_id=HUGGING_FACE_MODEL)
response = llm.invoke(prompt)

print("HuggingFace Response ::::::::")
print(response)
