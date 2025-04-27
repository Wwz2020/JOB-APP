# Turn "CV Job Matcher" into a Streamlit App

import streamlit as st
import fitz  # PyMuPDF for PDFs
import docx
import os

# Sample finance-related jobs
sample_jobs = [
    {"title": "Investment Analyst", "skills_required": ["Financial Modeling", "Valuation", "Investment Analysis"], "degree_required": "Master of Finance"},
    {"title": "Financial Analyst", "skills_required": ["Excel", "Financial Modeling"], "degree_required": "Bachelor"},
    {"title": "Investment Banking Associate", "skills_required": ["PowerPoint", "Valuation"], "degree_required": "Master of Finance"}
]

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page in pdf_document:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_cv_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        return extract_text_from_pdf("temp.pdf")
    elif uploaded_file.name.endswith(".docx"):
        with open("temp.docx", "wb") as f:
            f.write(uploaded_file.read())
        return extract_text_from_docx("temp.docx")
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")

def extract_qualifications(cv_text):
    skills_keywords = ["Excel", "Financial Modeling", "Valuation", "Investment Analysis", "PowerPoint", "Data Analysis"]
    degree_keywords = ["Bachelor", "Master", "PhD", "B.Sc", "M.Sc", "MBA", "Master of Finance"]
    experience_keywords = ["Analyst", "Intern", "Investment Banking", "Consultant", "Manager", "Associate"]

    skills_found = []
    degrees_found = []
    experiences_found = []

    for line in cv_text.split("\n"):
        for skill in skills_keywords:
            if skill.lower() in line.lower():
                skills_found.append(skill)
        for degree in degree_keywords:
            if degree.lower() in line.lower():
                degrees_found.append(degree)
        for experience in experience_keywords:
            if experience.lower() in line.lower():
                experiences_found.append(experience)

    return list(set(skills_found)), list(set(degrees_found)), list(set(experiences_found))

def match_jobs(skills, degrees):
    matched_jobs = []
    for job in sample_jobs:
        skill_match = any(skill in skills for skill in job["skills_required"])
        degree_match = any(degree in degrees for degree in [job["degree_required"]])
        if skill_match and degree_match:
            matched_jobs.append(job["title"])
    return matched_jobs

def generate_career_advice(skills, matched_jobs):
    recommended_skills = ["Financial Modeling", "Valuation", "Investment Analysis", "Excel", "PowerPoint"]
    missing_skills = [skill for skill in recommended_skills if skill not in skills]

    if matched_jobs:
        return "You are well-prepared for finance positions! Start applying and networking with professionals."
    elif skills:
        return "Consider improving the following skills: " + ", ".join(missing_skills) + "."
    else:
        return "Build basic finance skills like Financial Modeling, Excel, and Valuation to improve your career options."

def generate_cover_letter(name, job_title):
    return f"""Dear Hiring Manager,

My name is {name}, and I am excited to apply for the {job_title} position. With a strong background in finance, including expertise in Financial Modeling, Valuation, and Investment Analysis, I am confident in my ability to contribute effectively to your team.

My education at Johns Hopkins University (Master of Finance) and hands-on experience as a Financial Analyst Intern have equipped me with the analytical skills, attention to detail, and strategic thinking required for success in this role.

I would welcome the opportunity to further discuss how I can add value to your organization.

Thank you for your time and consideration.

Sincerely,
{name}
"""

# Streamlit App
st.title("📄 AI CV Matcher & Cover Letter Generator")

uploaded_file = st.file_uploader("Upload your resume (PDF or Word)", type=["pdf", "docx"])

if uploaded_file:
    cv_text = extract_cv_text(uploaded_file)
    skills, degrees, experiences = extract_qualifications(cv_text)

    st.subheader("Extracted Qualifications")
    st.write("**Skills:**", skills)
    st.write("**Degrees:**", degrees)
    st.write("**Experiences:**", experiences)

    matched_jobs = match_jobs(skills, degrees)

    st.subheader("Matched Job Opportunities")
    if matched_jobs:
        for job in matched_jobs:
            st.success(f"- {job}")
    else:
        st.warning("No matching jobs found.")

    st.subheader("Career Advice")
    advice = generate_career_advice(skills, matched_jobs)
    st.info(advice)

    st.subheader("Generate Cover Letter")
    name_input = st.text_input("Enter your full name:")

    if name_input and matched_jobs:
        cover_letter = generate_cover_letter(name_input, matched_jobs[0])
        st.text_area("Generated Cover Letter", cover_letter, height=300)
        st.download_button("Download Cover Letter", cover_letter, file_name=f"Cover_Letter_{matched_jobs[0].replace(' ', '_')}.txt")
