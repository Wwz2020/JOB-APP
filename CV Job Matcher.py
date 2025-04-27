import streamlit as st

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

    skills_found = list(set(skills_found))
    degrees_found = list(set(degrees_found))
    experiences_found = list(set(experiences_found))

    return skills_found, degrees_found, experiences_found

def match_jobs(skills, degrees, sample_jobs):
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
        advice = "You are well-prepared for finance positions! Start applying and networking with professionals in your target field."
    elif skills:
        advice = "We recommend improving the following skills to boost your job opportunities: " + ", ".join(missing_skills) + "."
    else:
        advice = "Consider building basic finance skills such as Financial Modeling, Excel, and Valuation to increase your career options."

    return advice

def generate_cover_letter(name, job_title):
    letter = f"""Dear Hiring Manager,

My name is {name}, and I am excited to apply for the {job_title} position. With a strong background in finance, including expertise in Financial Modeling, Valuation, and Investment Analysis, I am confident in my ability to contribute effectively to your team.

My education at Johns Hopkins University (Master of Finance) and hands-on experience as a Financial Analyst Intern have equipped me with the analytical skills, attention to detail, and strategic thinking required for success in this role.

I would welcome the opportunity to further discuss how I can add value to your organization.

Thank you for your time and consideration.

Sincerely,
{name}
"""
    return letter

# Sample Finance-related Jobs
sample_jobs = [
    {"title": "Investment Analyst", "skills_required": ["Financial Modeling", "Valuation", "Investment Analysis"], "degree_required": "Master of Finance"},
    {"title": "Financial Analyst", "skills_required": ["Excel", "Financial Modeling"], "degree_required": "Bachelor"},
    {"title": "Investment Banking Associate", "skills_required": ["PowerPoint", "Valuation"], "degree_required": "Master of Finance"}
]

# Streamlit App
st.title("\ud83d\udcc8 CV Analyzer for Finance Careers")

cv_text = st.text_area("Paste your CV text here:", height=300)

if st.button("Analyze CV"):
    if cv_text.strip() == "":
        st.warning("\ud83d\udeab Please paste your CV first.")
    else:
        skills, degrees, experiences = extract_qualifications(cv_text)

        st.subheader("Detected Skills:")
        st.write(skills if skills else "No skills detected.")

        st.subheader("Detected Degrees:")
        st.write(degrees if degrees else "No degrees detected.")

        st.subheader("Detected Experiences:")
        st.write(experiences if experiences else "No experiences detected.")

        matched_jobs = match_jobs(skills, degrees, sample_jobs)

        st.subheader("Matched Job Opportunities:")
        if matched_jobs:
            for job in matched_jobs:
                st.success(f"- {job}")
        else:
            st.info("No matching jobs found.")

        advice = generate_career_advice(skills, matched_jobs)

        st.subheader("Career Advice:")
        st.write(advice)

        if matched_jobs:
            name = st.text_input("Enter your name for the cover letter:")
            if name:
                cover_letter = generate_cover_letter(name, matched_jobs[0])
                st.subheader("Generated Cover Letter:")
                st.code(cover_letter)

                st.download_button("\ud83d\udcbe Download Cover Letter", cover_letter, file_name="Cover_Letter.txt")
