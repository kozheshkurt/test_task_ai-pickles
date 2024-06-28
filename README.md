# test_task_ai-pickles

Setup
Create a virtual environment:

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install dependencies:

pip install fastapi uvicorn langchain
Run the application:

uvicorn main:app --reload
Test the endpoint:

Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.