import fitz
import json
from resume_parser.genai_model import resume_details

def parser(uploaded_file):
    try:

        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        resume_text = ""
        hyperlinks = []

        for page in pdf_document:
            resume_text += page.get_text()  
            for link in page.get_links():
                if link.get('uri'):
                    hyperlinks.append(link.get('uri'))

        if not resume_text.strip():
            return {"error": "The PDF file does not contain any readable text."}

        response = resume_details(resume_text)
        response_clean = response.replace("```json", "").replace("```", "").strip()
        
        try:
            data = json.loads(response_clean)
            
            #Extracts hiperlinks if possible
            data["LinkedIn URL"] = next((link for link in hyperlinks if "linkedin" in link), "N/A")
            data["GitHub URL"] = next((link for link in hyperlinks if "github" in link), "N/A")
            data["LeetCode URL"] = next((link for link in hyperlinks if "leetcode" in link), "N/A")
            return data
        except json.JSONDecodeError:
            return {"error": "Failed to parse resume details."}

    except Exception as e:
        return {"error": f"An error occurred while reading the PDF: {str(e)}"}
