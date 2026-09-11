from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

response = llm.invoke("Hello, tell me one interesting fact about AI in one line.")
print(response.content)