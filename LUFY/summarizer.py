from langchain.llms import HuggingFacePipeline
from langchain.document_loaders import TextLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
import os
loader = TextLoader("./tasks.txt")
docs = loader.load()
# Define prompt
prompt_template = """Write a pointwise summary of the give text containg reviews:
"{text}"
CONCISE SUMMARY:"""
prompt = PromptTemplate.from_template(prompt_template)
llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 10,
                    "temperature": 0,},
)
llm_chain = LLMChain(llm=llm, prompt=prompt)
# Define StuffDocumentsChain
stuff_chain = StuffDocumentsChain(
    llm_chain=llm_chain, document_variable_name="text"
)
docs = loader.load()
print(stuff_chain.run(docs))