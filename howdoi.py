#!/usr/bin/env python3

import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys

if(len(sys.argv) == 1):
  print("Usage: howdoi <task>")
  sys.exit(0)

userInput = " ".join(sys.argv[1:])

load_dotenv()
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_TRACE"] = ""
apiKey = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = apiKey)
model = genai.GenerativeModel("gemini-1.5-flash")


prompt = """
You are a Linux command line expert. Your task is to provide the most relevant command for the following task. 
Include the command only and, if needed, brief comments or flags for clarity. Additionally, on the next line, 
provide a brief and concise explanation of the command's functionality. Do not wrap commands in triple backticks.
Provide the simplest command possible.
Task: """ + userInput
response = model.generate_content(prompt)
clean_text = response.text.replace("\n\n", "\n")
print(clean_text)
sys.exit(0)