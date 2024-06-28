from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from summarizer import SimpleSummarizer


class Request(BaseModel):
    initial_text: str


app = FastAPI()

model_id = "google/flan-t5-small"


@app.post("/summarize")
async def create_summary(request: Request):
    text_to_summarize = request.initial_text
    summarizer = SimpleSummarizer(model_id)
    summary = summarizer.summarize(text_to_summarize)
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)