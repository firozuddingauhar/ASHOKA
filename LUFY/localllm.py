from langchain.llms import ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ollama(model = "llama2",
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

llm("tell me 5 intresting facts about france")