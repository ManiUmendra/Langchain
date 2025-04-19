from config import LLAMA_MODEL, HUGGING_FACE_MODEL
from decouple import config
import os
from langchain_ollama.llms import OllamaLLM
#from langchain_community.llms import HuggingFaceEndPoint
from langchain_community.llms import HuggingFaceHub,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

os.environ['huggingfacehub_api_token'] = config('HUGGING_FACE_NEW_WRITE_TOKEN')

examples = [
    {
        "question": "Who lived longer, Muhammad Ali or Alan Turing?",
        "answer": """
Are follow up questions needed here: Yes.
Follow up: How old was Muhammad Ali when he died?
Intermediate answer: Muhammad Ali was 74 years old when he died.
Follow up: How old was Alan Turing when he died?
Intermediate answer: Alan Turing was 41 years old when he died.
So the final answer is: Muhammad Ali
""",
    },
    {
        "question": "When was the founder of craigslist born?",
        "answer": """
Are follow up questions needed here: Yes.
Follow up: Who was the founder of craigslist?
Intermediate answer: Craigslist was founded by Craig Newmark.
Follow up: When was Craig Newmark born?
Intermediate answer: Craig Newmark was born on December 6, 1952.
So the final answer is: December 6, 1952
""",
    },
    {
        "question": "Who was the maternal grandfather of George Washington?",
        "answer": """
Are follow up questions needed here: Yes.
Follow up: Who was the mother of George Washington?
Intermediate answer: The mother of George Washington was Mary Ball Washington.
Follow up: Who was the father of Mary Ball Washington?
Intermediate answer: The father of Mary Ball Washington was Joseph Ball.
So the final answer is: Joseph Ball
""",
    },
    {
        "question": "Are both the directors of Jaws and Casino Royale from the same country?",
        "answer": """
Are follow up questions needed here: Yes.
Follow up: Who is the director of Jaws?
Intermediate Answer: The director of Jaws is Steven Spielberg.
Follow up: Where is Steven Spielberg from?
Intermediate Answer: The United States.
Follow up: Who is the director of Casino Royale?
Intermediate Answer: The director of Casino Royale is Martin Campbell.
Follow up: Where is Martin Campbell from?
Intermediate Answer: New Zealand.
So the final answer is: No
""",
    },
]

promptTemplate = PromptTemplate(input_variables=['input','output'],template="Question : {question}\n{answer}")
prompt = FewShotPromptTemplate(examples=examples,example_prompt=promptTemplate,suffix="Question :{input}",input_variables=['input'])
messages = prompt.format(input="Who was the father of Mary Ball Washington?")

############## Ollama Model


model = OllamaLLM(model=LLAMA_MODEL)
response = model.invoke(messages)

print("Ollama Response:",response)


################### Hugging Face Model

model = HuggingFaceEndpoint(repo_id=HUGGING_FACE_MODEL)
response = model.invoke(messages)

print("Hugging Face Response:",response)