from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama
from config import LLAMA_MODEL
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

history = ChatMessageHistory()
history.add_ai_message("hi")
history.add_user_message("Hello")
print("For Chat Message History::::::::::::::::::::::::::::::::::")
print(history)


################# For Conversation Buffer Memory

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a chatbot having a conversation with a human."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{input}")
])

runnable = prompt | ChatOllama(model=LLAMA_MODEL)

store = {}
def get_session_history(session_id) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain = RunnableWithMessageHistory(
    runnable,get_session_history,input_messages_key="input",history_messages_key="chat_history"
)

result = chain.invoke({
    "input":"hi"
},config={"configurable":{"session_id":"abc"}})

print(result)
print(store)