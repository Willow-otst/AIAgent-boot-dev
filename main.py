# Get api key from env variable
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# import the genai library using the imported key
from google import genai
client = genai.Client(api_key=api_key)

# other imports
import sys

# main
if len(sys.argv) <= 1:
    print("ERROR - Please provide a prompt.")
    exit(1)

prompt = sys.argv[1]
response = client.models.generate_content(
    model= 'gemini-2.0-flash-001',
    contents= prompt
)
print(response.text + "\n")
print(
    f"Tokens: (Prompt: {response.usage_metadata.prompt_token_count})" +
    f"(Respnse: {response.usage_metadata.candidates_token_count})"
)
