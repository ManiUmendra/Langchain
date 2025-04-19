from langchain_community.chat_models import ChatOllama
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field
from config import LLAMA_MODEL
import os

class Crickter(BaseModel):
    name : str = Field(description="Name of the crcketer.")
    recods : list = Field(description="List of recods")

messages = "{request} \n {format_instructions}"

promptTemplate = ChatPromptTemplate.from_messages([
    ('human',messages),
])
parser = PydanticOutputParser(pydantic_object=Crickter)

prompt = promptTemplate.format_messages(
    request = "tell me about cricketer",
    format_instructions = parser.get_format_instructions()
)

model = ChatOllama(model=LLAMA_MODEL)

response = model.invoke(prompt)
print(parser.parse(response.content))
