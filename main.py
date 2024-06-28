from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from summarizer import SimpleSummarizer #class, created in different file


# describe the model of data, get from post request
class Request(BaseModel):
    initial_text: str


app = FastAPI()

# variable with the used model to have a possibility of using different models
model_id = "google/flan-t5-small"


@app.post("/summarize")
async def create_summary(request: Request):
    text_to_summarize = request.initial_text    #get text from request
    summarizer = SimpleSummarizer(model_id)     #create an instance of SimpleSummarizer class from the file summarizer.py
    summary = summarizer.summarize(text_to_summarize)  #get the summary by summarize method of SimpleSummarizer class
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) #run the server