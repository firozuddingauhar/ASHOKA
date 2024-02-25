import requests
import json

SERP_KEY="42d0003140eb86be6b29cf08e83a7772be036b1c"

def search_internet_(query):
  url = "https://google.serper.dev/search"
  payload = json.dumps({
    "q":query
  })
  headers = {
    'X-API-KEY' : SERP_KEY,
    'Content-Type' : 'application/json'
  }
  response = requests.request("POST",url,headers=headers,data=payload)
  response_data =  response.json()
  print("search results: ", response_data["answerBox"]["snippet"])
  print("\n", response_data["answerBox"]["snippetHighlighted"][0])
  return response_data

search_internet_(input("serch for: "))

# from langchain.agents import load_tools
# from langchain.agents import initialize_agent
# from langchain.llms import OpenAI
# from langchain.agents import load_tools

# # import os
# # from dotenv import load_datenv
# # load_datenv()
# # os.getenv('OPENAI_API_KEY')

# # os.environ['OPENAI_API_KEY'] = "..."
# # os.environ['SERPAPI_API_KEY'] = "..."

# llm = OpenAI(temperature=0)
# tool_names = ["serpapi"]
# tools = load_tools(tool_names)

# agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
# agent.run("What is langchain?")