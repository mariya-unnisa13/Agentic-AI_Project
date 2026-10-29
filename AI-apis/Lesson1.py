import os
from dotenv import load_dotenv
from google import genai
 
load_dotenv()
 
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
 
response = client.models.generate_content(
    model="gemini-3.8-flash",   # use the current name shown in AI Studio
    contents="Explain SAP"
    contents="Main Features"
    contents="Use Cases and Pros/Cons"
)
 
print(response.text)