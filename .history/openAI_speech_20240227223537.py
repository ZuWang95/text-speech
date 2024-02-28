import sys
import os
import re
from openai import OpenAI
from pathlib import Path

OpenAI.api_key = os.getenv('OPENAI_API_KEY')

argc = len(sys.argv)

if argc < 2:
    error_message = "python input_video_script_file (tex)"
    print(error_message)
    raise Exception(error_message)

input_video_script_file = sys.argv[1]

fin = open(input_video_script_file, 'r')
lines = fin.read()

audios = re.findall('\\\\audio\s*\[(.*?)\]\s*{(.*?)}', lines, re.DOTALL)

client = OpenAI()
# Iterate over each text portion
for i, text in enumerate(audios, start=1):
    # Call the OpenAI Text-to-Speech API
    response = client.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input=text
    )

    # Define the path for the output audio file
    speech_file_path = Path(f"speech_{i}.mp3")
    
    # Save the audio content to a file
    response.with_streaming_response(str(speech_file_path))

    print(f"Saved speech to {speech_file_path}")