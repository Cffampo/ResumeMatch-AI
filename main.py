import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import re
import pandas as pd
import json

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# st.subheader("Available Gemini Models")

# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         st.write(m.name)
model = genai.GenerativeModel("models/gemini-flash-lite-latest")

# Streamlit app configuration
st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")
st.title("ResumeMatch AI")
st.caption("Compare your resume against a job description and get ATS-style feedback.")

uploaded_file = st.file_uploader("Upload your PDF resume", type=["pdf"])

if uploaded_file:
    pdf = PdfReader(uploaded_file)
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Clean up the extracted text by replacing single newlines with spaces, while preserving paragraph breaks (double newlines)
    text_clean = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Resume Preview")

        # Use an expander to show the extracted resume text, allowing users to hide it if they want
        with st.expander("View Extracted Resume Text", expanded=False):
            st.text_area("Extracted Resume Text", value=text_clean, height=400)

    with col2:
        st.subheader("AI Analysis")

        job_desc = st.text_area("Optional: Paste a job description here to tailor the analysis", height=150, placeholder="Paste the job posting here...")

        if st.button("Analyze Resume", use_container_width=True):
            with st.spinner("Analyzing your resume..."):
                prompt = f"""
You are a career coach. Analyze the following resume and provide:

1. A concise summary of the candidate's experience and qualifications.
2. A list of key skills and competencies.
3. Suggestions for improvement to make the resume more appealing to recruiters.
4. A score out of 100 based on:
   - skills match: 30 points
   - experience and achievement: 30 points
   - formatting and presentation: 20 points
   - overall impression: 20 points

At the end, include this exact label:
Score JSON:

Then provide only valid JSON in this format:
{{
  "Skills Match": 0,
  "Experience and Achievement": 0,
  "Formatting and Presentation": 0,
  "Overall Impression": 0
}}

Compare this resume against the following job description.

Job Description:
{job_desc}

Resume:
{text_clean}
"""

# Send the prompt to Gemini and handle the response with error handling
                try:
                    response = model.generate_content(prompt)
                    result = response.text

                    st.download_button(
                        label="Download Analysis Report",
                        data=result,
                        file_name="resume_analysis.txt",
                        mime="text/plain"
                    )

                    parts = result.split("Score JSON:")
                    analysis_text = parts[0]
                    st.write(analysis_text)


                    # Try to parse the score JSON if it exists
                    if len(parts) > 1: # Check if the score JSON part exists
                        try:
                            score_json = json.loads(parts[1].strip()) # Parse the JSON part

                            st.subheader("Resume Score")

                            # Convert the score JSON into a DataFrame for visualization
                            score_df = pd.DataFrame({
                                "Category": list(score_json.keys()), 
                                "Score": list(score_json.values())
                            })

                            # Display the scores as a bar chart
                            st.bar_chart(score_df.set_index("Category"))

                            st.subheader("Overall Score")
                            total_score = sum(score_json.values())
                            st.progress(min(total_score / 100, 1.0))
                            st.write(f"Total Score: {total_score}/100")

                        except:
                            st.warning("Could not parse score JSON from the AI response.")

                except Exception as e:
                    st.error(f"Gemini API Error: {e}")