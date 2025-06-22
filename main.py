import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

verbose = False;

if len(sys.argv) <= 1:
    print("ERROR - Please provide a prompt.")
    exit(1)
for arg in sys.argv[1:]:
    if arg in ["-v", "--verbose"]:
        verbose = True;
        sys.argv.remove(arg)
        continue
prompt = sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [types.Content(
    role = "user",
    parts = [types.Part(text = prompt)]),]

response = client.models.generate_content(
    model = 'gemini-2.0-flash-001',
    contents = messages)

print(response.text + "\n")

if verbose:
    print("============================================")
    print(f"Prompt: {prompt}\n")
    print(
        f"Tokens: (Prompt: {response.usage_metadata.prompt_token_count})" +
        f"(Respnse: {response.usage_metadata.candidates_token_count})"
    )
    print("User prompt: Prompt tokens: Response tokens:")
