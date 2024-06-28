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


# test case if the script is called directly
if __name__ == "__main__":
    summarizer = SimpleSummarizer("google/flan-t5-small")
    test_text = '''
    Introduction. The liver is known to be one of the central organs of metabolic regulation, as it provides both synthesis of a significant number of macromolecules and modification, decomposition and detoxification of a lot of metabolites and xenobiotics. Disruption of the balance between these processes in the liver is usually accompanied by changes in its structural and functional characteristics, and in case of long-term deviations from the homeostatic norm, pathological processes take place.  Pathological changes in the liver can be induced by extremely various biological (viruses, bacteria), physical and chemical factors.
    Pathological processes in the liver, independent of the pathogenetic factor, go through a number of consistent stages: hepatitis, fibrosis, cirrhosis and/or carcinogenesis. Currently, mortality from liver diseases ranks 5th in the world. The study of the mechanisms of formation and development of liver fibrosis is the basis for the development of ways to prevent and treat liver diseases. Such fundamental studies can be carried out only on experimental animal models. Although there is an intensive search for modern methods of evaluating the functional state of the liver, morphological studies are still the gold standard in hepatological diagnostics. However, establishing a diagnosis at early or initial stages, significant changes in structural and functional characteristics that may lead to fibrosis in the future is very difficult, and most often impossible.
    '''
    test_summary = summarizer.summarize(test_text)
    print(test_summary)
