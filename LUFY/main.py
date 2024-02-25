# from langchain.llms import HuggingFacePipeline
# from langchain.document_loaders import TextLoader
# from langchain.chains.summarize import load_summarize_chain
# from langchain.chains.llm import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain.chains.combine_documents.stuff import StuffDocumentsChain
# import os
# loader = TextLoader("./review.txt")
# docs = loader.load()
# # Define prompt
# prompt_template = """Write a pointwise summary of the give text containg reviews:
# "{text}"
# CONCISE SUMMARY:"""
# prompt = PromptTemplate.from_template(prompt_template)
# llm = HuggingFacePipeline.from_model_id(
#     model_id="gpt2",
#     task="text-generation",
#     pipeline_kwargs={"max_new_tokens": 10,
#                     "temperature": 0,},
# )
# llm_chain = LLMChain(llm=llm, prompt=prompt)
# # Define StuffDocumentsChain
# stuff_chain = StuffDocumentsChain(
#     llm_chain=llm_chain, document_variable_name="text"
# )
# docs = loader.load()
# print(stuff_chain.run(docs))


# import json
# import requests
# headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZWQ0ODZjYjUtNmZiMi00N2QxLTg5NjktMzI4NTAxZjcyMzdhIiwidHlwZSI6ImFwaV90b2tlbiJ9.3Dcqr9qrdDCtFqzoK_pyOod92kwkLnGsuvGQS8r6FXA"}
# url ="https://api.edenai.run/v2/text/generation"
# payload = {
#       "providers": "openai,cohere",
#       "text": "what is the smart india hackathon",
#       "temperature" : 0.2,
#       "max_tokens" : 250
#     }
# response = requests.post(url, json=payload, headers=headers)
# result = json.loads(response.text)
# print(result['openai']['generated_text'])


# # internet search
# import requests
# import json
# SERP_KEY="42d0003140eb86be6b29cf08e83a7772be036b1c"
# def search_internet_(query):
#   url = "https://google.serper.dev/search"
#   payload = json.dumps({
#     "q":query
#   })
#   headers = {
#     'X-API-KEY' : SERP_KEY,
#     'Content-Type' : 'application/json'
#   }
#   response = requests.request("POST",url,headers=headers,data=payload)
#   response_data =  response.json()
#   print("search results: ", response_data["answerBox"]["snippet"])
#   print("\n", response_data["answerBox"]["snippetHighlighted"][0])
#   return response_data
# search_internet_(input("serch for: "))

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from translate import Translator
import time
userquery = input("enter promt: ")
start = time.time()
persist_directory = 'db'
embedding = HuggingFaceEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, 
                  embedding_function=embedding)
retriever = vectordb.as_retriever()
docs = retriever.get_relevant_documents(userquery)
end = time.time()
print ("Time elapsed:", end - start)
print(docs)
# print(Translator(from_lang="en",to_lang="hindi").translate(docs))