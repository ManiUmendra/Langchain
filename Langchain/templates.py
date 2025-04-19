from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

##### Prompt Template

messages = "Tell me a {adjective} joke about {content}."

promptTemplate = PromptTemplate.from_template(messages)
prompt = promptTemplate.format(adjective="joke",content="man")

print("Tuple = ",prompt)


##### ChatPrompt Template

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)

messages = chat_template.format_messages(name="Bob", user_input="What is your name?")
print(messages)
