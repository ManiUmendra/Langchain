from config import LLAMA_MODEL
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import HumanMessage,SystemMessage

model = OllamaLLM(model=LLAMA_MODEL)
print(model)
question = "Who is the prime minister of India?"

#Not Runnable
# messages = [
#     SystemMessage(content="You're a helpful assistant"),
#     HumanMessage(content="What is the purpose of model regularization?")
# ]
response = model.invoke(question)
print(response)