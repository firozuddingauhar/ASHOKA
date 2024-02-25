import requests
import json

SERP_KEY="42d0003140eb86be6b29cf08e83a7772be036b1c"

def search(query):
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
  print("search results: ", response_data["answerBox"]["snippetHighlighted"])
  return response_data

search("what is smart india hackathone")