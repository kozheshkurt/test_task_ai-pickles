from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFacePipeline
import auth

class SimpleSummarizer():

    def __init__(self, model_id: str):
        self.llm = HuggingFacePipeline.from_model_id(
            model_id = model_id,
            task = "summarization",
        )


    def summarize(self, text_to_summarize: str):
        
        messages = [
            SystemMessage(content="Write a concise summary of the following:"),
            HumanMessage(content=text_to_summarize),
        ]

        summary = self.llm.invoke(messages)
        return summary

