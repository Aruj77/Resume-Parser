import streamlit as st
import json
from io import BytesIO
from resume_parser.parse_resume import parser

st.set_page_config(page_title="FactoryKaam", page_icon="🛠️")

def resume_formatter(data):
    formatted_data = f"""
**Full Name**: {data.get("Full Name", "N/A")}

**Contact Number**: {data.get("Contact Number", "N/A")}

**Email Address**: {data.get("Email Address", "N/A")}

**Location**: {data.get("Location", "N/A")}

**Technical Skills**: {', '.join(data["Skills"].get("Technical Skills", [])) if "Skills" in data else 'N/A'}

**Non-Technical Skills**: {', '.join(data["Skills"].get("Non-Technical Skills", [])) if "Skills" in data else 'N/A'}

**Education**:
"""
    for edu in data.get("Education", []):
        formatted_data += f"- {edu.get('degree', 'N/A')} from {edu.get('institution', 'N/A')} (Graduated: {edu.get('graduation year', 'N/A')})\n"

    formatted_data += "\n**Work Experience**:\n"
    for job in data.get("Work Experience", []):
        formatted_data += f"- {job.get('role', 'N/A')} at {job.get('company name', 'N/A')} ({job.get('years of experience', 'N/A')})\n"
        formatted_data += f"  Responsibilities: {job.get('responsibilities', 'N/A')}\n"

    formatted_data += f"\n**Certifications**: {', '.join(data.get('Certifications', [])) if data.get('Certifications') else 'N/A'}\n"
    formatted_data += f"\n**Languages**: {', '.join(data.get('Languages spoken', [])) if data.get('Languages spoken') else 'N/A'}\n"
    
    formatted_data += f"\n**LinkedIn**: {data.get('LinkedIn URL', 'N/A')}\n"
    formatted_data += f"\n**GitHub**: {data.get('GitHub URL', 'N/A')}\n"
    formatted_data += f"\n**LeetCode**: {data.get('LeetCode URL', 'N/A')}\n"
    return formatted_data

def create_download_link(data, filename="resume_details.json"):
    json_data = json.dumps(data, indent=4)
    b = BytesIO(json_data.encode())
    return b

st.title("Resume Parser")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type="pdf")

# If a file is uploaded, parse and display the resume details
if uploaded_file is not None:
    resume_data = parser(uploaded_file)
    
    if "error" in resume_data:
        st.error(resume_data["error"])
    else:
        st.subheader("Parsed Resume Details:")
        
        # Formatted data displayed
        st.markdown(resume_formatter(resume_data))
        
        download_buffer = create_download_link(resume_data)
        st.download_button(
            label="Download (JSON)",
            data=download_buffer,
            file_name="resume_details.json",
            mime="application/json"
        )
else:
    st.info("Please upload resume in PDF only.")
