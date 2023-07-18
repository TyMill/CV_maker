class ContactInfo:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Summary:
    def __init__(self, summary):
        self.summary = summary

class Experience:
    def __init__(self, job_title, company, start_date, end_date, bullet_points):
        self.job_title = job_title
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.bullet_points = bullet_points

class Skills:
    def __init__(self, skill_list):
        self.skill_list = skill_list

class Education:
    def __init__(self, degree, institution, start_date, end_date):
        self.degree = degree
        self.institution = institution
        self.start_date = start_date
        self.end_date = end_date

def generate_markdown(cv):
    markdown = f"# {cv['contact'].name}\n"
    markdown += f"Email: {cv['contact'].email} | Phone: {cv['contact'].phone}\n\n"

    markdown += "## Summary\n"
    markdown += f"{cv['summary'].summary}\n\n"

    markdown += "## Experience\n"
    for job in cv['experience']:
        markdown += f"### {job.job_title}, {job.company} ({job.start_date} - {job.end_date})\n"
        for bullet in job.bullet_points:
            markdown += f"- {bullet}\n"
        markdown += "\n"

    markdown += "## Skills\n"
    for skill in cv['skills'].skill_list:
        markdown += f"- {skill}\n"
    markdown += "\n"

    markdown += "## Education\n"
    for edu in cv['education']:
        markdown += f"- {edu.degree}, {edu.institution} ({edu.start_date} - {edu.end_date})\n"
    markdown += "\n"

    return markdown

def main():
    contact = ContactInfo("......", "....", "....")
    summary = Summary("I'm a data freak...")
    experience = [Experience("Data Scientist Consultant", "....", "...., "Present", ["Developed and deployed machine learning models...", "Conducted data preprocessing..."]), Experience("Pricing Expert / Data Science Manager", "......", "Start Date", "End Date", ["Performed complex analyses of price lists...", "Designed, developed and implemented data-driven pricing strategies..."])]
    skills = Skills(["Financial Forecasting", "Communication", "Problem Solving", "Pattern Recognition", "Project Planning", "Artificial Intelligence", "Data Collection", "Biostatistics", "Interpersonal Skills", "Unsupervised Learning", "Data Visualization", "Causal Inference", "Python", "Machine Learning"])
    education = [Education("Postgraduate Degree, Kontroler finansowy", "Akademia Leona Koźmińskiego (Kozminski University)", "Oct 2021", "Jun 2022"), Education("Postgraduate Degree, Data Scientist - Big Data i Systemy zaawansowanej analizy danych", "......", "Oct 2020", "May 2021"), Education("......", "Uniwersytet Szczeciński", "....", "...."), Education("Postgraduate, ......", "Uniwersytet WSB Szczecin", "2019", "2020"), Education("Master's degree, Biology/Biological Sciences, General", "Uniwersytet Szczeciński", "2006", "2011")]

    cv = {
        "contact": contact,
        "summary": summary,
        "experience": experience,
        "skills": skills,
        "education": education
    }

    markdown_cv = generate_markdown(cv)

    with open("CV.md", "w") as file:
        file.write(markdown_cv)

if __name__ == "__main__":
    main()
