import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

def resume_details(resume_text):
    prompt = f"""
    You are a resume parsing assistant. Extract the following details from the given resume text. Ensure to return "N/A" if information is missing or unclear.
    
    Resume text:
    {resume_text}
    
    Extract and include the following in a structured JSON format:
    1. Full Name
    2. Contact Number
    3. Email Address
    4. Location
    5. Skills (separate Technical and Non-Technical Skills)
    6. Education (degree, institution, graduation year)
    7. Work Experience (company name, role, responsibilities, years of experience)
    8. Certifications
    9. Languages spoken
    10. LinkedIn URL
    11. GitHub URL
    12. LeetCode URL
    """

    response = model.generate_content(prompt).text
    return response
