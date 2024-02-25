import os
import chainlit as cl
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from getpass import getpass

# HUGGINGFACEHUB_API_TOKEN = getpass()
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"

model_id = "gpt2-medium"
conv_model = HuggingFaceHub(huggingfacehub_api_token=
                            os.environ['HUGGINGFACEHUB_API_TOKEN'],
                            repo_id=model_id,
                            model_kwargs={"temperature":0.8, "max_new_tokens":150})

template = """You are a helpful AI assistant that answers the law related questions query received as input

{query}
"""


@cl.on_chat_start
def main():
    prompt = PromptTemplate(template=template, input_variables=['query'])
    conv_chain = LLMChain(llm=conv_model,
                          prompt=prompt,
                          verbose=True)
    
    cl.user_session.set("llm_chain", conv_chain)
    
@cl.on_message
async def main(message:str):
    llm_chain = cl.user_session.get("llm_chain")
    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])
    
    await cl.Message(content=res["text"]).send()