# CV Analyzer - Finance Focused - Complete Version (with Saving Cover Letter)

def get_cv_text():
    print("Please paste your CV text below (end with a single line 'END'):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

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

def save_cover_letter(cover_letter_text, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(cover_letter_text)
    print(f"\nCover letter saved successfully as '{filename}'!")

# Sample Finance-related Jobs
sample_jobs = [
    {
        "title": "Investment Analyst",
        "skills_required": ["Financial Modeling", "Valuation", "Investment Analysis"],
        "degree_required": "Master of Finance"
    },
    {
        "title": "Financial Analyst",
        "skills_required": ["Excel", "Financial Modeling"],
        "degree_required": "Bachelor"
    },
    {
        "title": "Investment Banking Associate",
        "skills_required": ["PowerPoint", "Valuation"],
        "degree_required": "Master of Finance"
    }
]

# Main execution
if __name__ == "__main__":
    cv_text = get_cv_text()

    print("\n=== Extracted CV Text ===")
    print(cv_text)

    skills, degrees, experiences = extract_qualifications(cv_text)

    print("\n=== Detected Skills ===")
    print(skills)

    print("\n=== Detected Degrees ===")
    print(degrees)

    print("\n=== Detected Experiences ===")
    print(experiences)

    matched_jobs = match_jobs(skills, degrees, sample_jobs)

    print("\n=== Matched Job Opportunities ===")
    if matched_jobs:
        for job in matched_jobs:
            print(f"- {job}")
    else:
        print("No matching jobs found.")

    # Generate Career Advice
    advice = generate_career_advice(skills, matched_jobs)
    print("\n=== Career Advice ===")
    print(advice)

    # Generate and Save Cover Letter
    if matched_jobs:
        name = input("\nEnter your name for the cover letter: ")
        cover_letter = generate_cover_letter(name, matched_jobs[0])
        print("\n=== Generated Cover Letter ===")
        print(cover_letter)

        filename = "Cover_Letter.docx"
        save_cover_letter(cover_letter, filename)
    else:
        print("\nNo cover letter generated since no matching jobs were found.")
