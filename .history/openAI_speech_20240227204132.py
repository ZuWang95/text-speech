import os

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
print(os.environ.get("OPENAI_API_KEY")) #key should now be available