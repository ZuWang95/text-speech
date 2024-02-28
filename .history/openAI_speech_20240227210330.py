import sys
import os
import re
from openai import OpenAI
from pathlib import Path


client = OpenAI()

argc = len(sys.argv)

if argc < 2:
    error_message = "python input_video_script_file (tex)"
    print(error_message)
    raise Exception(error_message)
input_video_script_file = sys.argv[1]

fin = open(input_video_script_file, 'r')
lines = fin.read()




speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)