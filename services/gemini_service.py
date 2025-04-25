import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def get_gemini_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        print("✅ Gemini raw response:", response)
        return response.text
    except Exception as e:
        print("❌ Gemini Error:", e)
        raise

