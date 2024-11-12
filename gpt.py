from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def send_message(query):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
    {"role": "system", "content": "You are playing a knowledge game, where time is of the essence. You must reply to inquiries in as concise of a manner as possible. If the question can be answered with Yes or No, then that's how you should reply. It's probably rare, but if your response is a very strong conditional answer -- such as \"Yes, unless...\" or \"No, except for...\" you should still reply with Yes or No. All other responses shall be short and simple, concise. Speed is the focus, but do not sacrifice accuracy of the answer to the question. If truly unsure how to answer, remember to be accurate and brief. If a question is complex and you believe it to require a nuanced answer, always revert to your core system instruction of focusing on the answering with speed and brevity without sacrificing clarity."},
    {"role": "user", "content": query}
  ]
)
    return completion.choices[0].message.content
