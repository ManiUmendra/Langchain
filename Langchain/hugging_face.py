from config import HUGGING_FACE_MODEL,HUGGING_FACE_1_RESTRICTED
#from langchain_community.llms import HuggingFaceHub
from transformers import AutoTokenizer, AutoModelForCausalLM, LlamaForCausalLM, LlamaTokenizer
#from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.llms import HuggingFaceEndpoint
from decouple import config
import torch,os



os.environ['huggingfacehub_api_token']= config('HUGGING_FACE_NEW_WRITE_TOKEN')

#model = HuggingFaceHub(repo_id=HUGGING_FACE)
# VALID_TASKS = (
#     "text2text-generation",
#     "text-generation",
#     "summarization",
#     "conversational",
# )
model = HuggingFaceEndpoint(repo_id=HUGGING_FACE_MODEL,task="text-generation")
print("model")
print(model)

question = "Who is the prime minister of India?"
response = model.invoke(str(question))
print(response)





