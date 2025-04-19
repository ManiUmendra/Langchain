#################### For Text File Loader

from langchain_community.document_loaders import TextLoader

# text_loader = TextLoader('C:\\Users\\umend\\OneDrive\\Documents\\Datas\\text.txt')
# text = text_loader.load()

# print(text[0].page_content)


#################### For PDF File Loader

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from config import LLAMA_MODEL

pdf_loader = PyPDFLoader('C:\\Users\\umend\\OneDrive\\Documents\\Datas\\PwC\\PwC+AC+Bangalore+Offer+-+Intern+2023-02-21.pdf')
pdf_content = pdf_loader.load()

model = ChatOllama(model=LLAMA_MODEL)

context = pdf_content[0].page_content

prompt = """
    Question: {question}

    Based on the context provided:
    {context}

    Answer:"""

promptTemplate = ChatPromptTemplate.from_messages([
    ('human',prompt)
])
prompt = promptTemplate.format_messages(
    question="how much stipend is being offered?",
    context=context,
)
#print(prompt)
response = model.invoke(prompt)

print(response.content)

