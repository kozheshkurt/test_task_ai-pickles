# test_task_ai-pickles

## Setup

1. Create a virtual environment:
   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn langchain langchain_huggingface
   ```

3. To performprovide authorization in HuggingFace, create file `auth.py`, get the Hugging Face Access Token (https://huggingface.co/docs/hub/security-tokens) and paste it into the `auth.py`:
   ```python
   import os
   os.environ['HUGGINGFACEHUB_API_TOKEN'] = "hf_.............."
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Test the endpoint:
   - Optionally. `summarizer.py` contains test case with the default text, the summary of which is printed by direct calling the file:
   ```bash
   python summarizer.py
   ```
   - Send a POST request to `http://127.0.0.1:8000/summarize` with a JSON body containing the text to be summarized:
   ```json
   {
   "initial_text": "string"
   }
   ```
