import getpass
import os
from langchain_community.tools.tavily_search import TavilySearchResults


os.environ["TAVILY_API_KEY"] = "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"
print("hehh")

tool = TavilySearchResults()

val = tool.invoke({"query": "What happened in the latest burning man floods"})
print(val)
