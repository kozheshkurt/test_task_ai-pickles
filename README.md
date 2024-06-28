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

3. To perform authorization in HuggingFace creat file 'auth.py', get the Hugging Face Access Token (https://huggingface.co/docs/hub/security-tokens) and paste it into the 'auth.py':
   ```
   import os
   os.environ['HUGGINGFACEHUB_API_TOKEN'] = "hf_.............."
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Test the endpoint:
   - Send a POST request to `http://127.0.0.1:8000/summarize` with a JSON body containing the text to be summarized.