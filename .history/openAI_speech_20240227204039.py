import sys
import os
import re
from openai import OpenAI

os.environ[“OPENAI_API_KEY”] = “your key here”
client = OpenAI()