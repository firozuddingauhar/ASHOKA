# from langchain.vectorstores import Chroma
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import PyPDFLoader
# from langchain.document_loaders import DirectoryLoader

# import os
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

# loader = DirectoryLoader('./data_documents/', glob="./*.pdf", loader_cls=PyPDFLoader)
# documents = loader.load()

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# texts = text_splitter.split_documents(documents)

# persist_directory = 'db'

# embedding = HuggingFaceEmbeddings()
# vectordb = Chroma.from_documents(documents=texts, embedding=embedding,
#                                  persist_directory=persist_directory)

# vectordb.persist()
# vectordb = None
 
# vectordb = Chroma(persist_directory=persist_directory, 
#                   embedding_function=embedding)
# retriever = vectordb.as_retriever()
# docs = retriever.get_relevant_documents("section 25A of the Code of Criminal Procedure?")
# print(docs)



# # create the chain to answer questions 
# qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), 
#                                   chain_type="stuff", 
#                                   retriever=retriever, 
#                                   return_source_documents=True)
# ## Cite sources
# def process_llm_response(llm_response):
#     print(llm_response['result'])
#     print('\n\nSources:')
#     for source in llm_response["source_documents"]:
#         print(source.metadata['source'])
# # full example
# query = "How much money did Pando raise?"
# llm_response = qa_chain(query)
# process_llm_response(llm_response)
