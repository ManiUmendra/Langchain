from config import LLAMA_MODEL
from langchain_community.chat_models import ChatOllama
#from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import HumanMessage,SystemMessage

# model1 = OllamaLLM(model=LLAMA_MODEL)
model = ChatOllama(model=LLAMA_MODEL,temperature=0)
print(model)
# question = "Who is the prime minister of India?"

messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="Who is the prime minister of India?")
]
response = model.invoke(messages)
print(response.content)


#llm = ChatOllama()
