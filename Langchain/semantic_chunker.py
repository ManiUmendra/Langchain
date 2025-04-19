from langchain_ollama import OllamaEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from config import LLAMA_MODEL

text = '''Artificial intelligence (AI) is transforming industries around the world. In healthcare, AI is used to diagnose diseases and recommend treatments. In finance, AI algorithms detect fraudulent activities and predict market trends. Education is also benefiting from AI through personalized learning and automated grading.
'''
# splitter_percentile = SemanticChunker(OllamaEmbeddings(model=LLAMA_MODEL),breakpoint_threshold_type='percentile')
# docs_percentile = splitter_percentile.create_documents([text])

# print("Percentile :::::::::::::::::::::")
# print(docs_percentile)


# splitter_interquartile = SemanticChunker(OllamaEmbeddings(model=LLAMA_MODEL),breakpoint_threshold_type='interquartile')
# docs_interquartile = splitter_interquartile.create_documents([text])

# print()
# print("Interquartile :::::::::::::::::::::")
# print(docs_interquartile)


splitter_standard_deviation = SemanticChunker(OllamaEmbeddings(model=LLAMA_MODEL),breakpoint_threshold_type='standard_deviation',number_of_chunks=3)
docs_standard_deviation = splitter_standard_deviation.create_documents([text])

print()
print("Standard Deviation :::::::::::::::::::::")
print(docs_standard_deviation)