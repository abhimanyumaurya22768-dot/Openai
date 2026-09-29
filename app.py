
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Check whether the API key exists
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing from .env")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Send request to the model
response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain artificial intelligence in complex terms."
)

# Display the response
print(response.output_text)