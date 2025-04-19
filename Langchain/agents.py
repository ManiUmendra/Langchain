from config import LLAMA_MODEL
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader,WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import create_tool_calling_agent,AgentExecutor
from langchain_community.chat_models.ollama import ChatOllama

import os
from langchain import hub
from langchain_ollama import OllamaLLM
# import langchainhub


os.environ["TAVILY_API_KEY"] = "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"

llm = ChatOllama(model=LLAMA_MODEL)
# embeddings = OllamaEmbeddings(model=LLAMA_MODEL)

# data = WebBaseLoader("https://docs.smith.langchain.com/overview")
# docs = data.load()

# print(docs)

# split = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
# vector = FAISS.from_documents(documents=split,embedding=embeddings)

# vector.save_local('web_data')
#retreiver = vector.as_retriever()
retriever = FAISS.load_local('web_data',OllamaEmbeddings(model=LLAMA_MODEL),allow_dangerous_deserialization=True).as_retriever()

retriever_tool = create_retriever_tool(retriever,"langsmith","Search for information about LangSmith. For any questions about LangSmith, you must use this tool!")
# res=retriever.invoke("how to upload a dataset")

print("Data has been loaded")

tavily = TavilySearchResults()

tools = [tavily,retriever_tool]

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")
print(prompt)
# agent = create_tool_calling_agent(llm,tools,prompt)

# exec = AgentExecutor(agent=agent,tools=tools,verbose=True)
# val  = exec.invoke({"input": "hi!"})
# print(val)

