from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from config import LLAMA_MODEL
from operator import itemgetter

model = ChatOllama(model=LLAMA_MODEL)

chat_1 = ChatPromptTemplate.from_template("what is the city {person} is from?")
chat_2 = ChatPromptTemplate.from_template("what country is the city {city} in? respond in {language}")
#print(model)
city_chain = chat_1 | model
country_chain = (
    {"city":city_chain,"language":itemgetter("lang")} | chat_2 | model
)

result = country_chain.batch([{'person':'Virat Kohli',"lang":"english"},{'person':'Jos Buttler',"lang":"english"}])
print(result)



