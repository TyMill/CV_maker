contact = ContactInfo("......", ".....", "....")
summary = Summary("I'm a data freak...")
experience = [Experience("Data Scientist Consultant", "Miller Consulting Tymoteusz Miller", "May 2019", "Present", ["Developed and deployed machine learning models...", "Conducted data preprocessing..."]), Experience("Pricing Expert / Data Science Manager", "NordGlass Sp. z o.o. (B2B)", "Start Date", "End Date", ["Performed complex analyses of price lists...", "Designed, developed and implemented data-driven pricing strategies..."])]
skills = Skills(["Financial Forecasting", "Communication", "Problem Solving", "Pattern Recognition", "Project Planning", "Artificial Intelligence", "Data Collection", "Biostatistics", "Interpersonal Skills", "Unsupervised Learning", "Data Visualization", "Causal Inference", "Python", "Machine Learning"])
education = [Education("Postgraduate Degree, Kontroler finansowy", "Akademia Leona Koźmińskiego (Kozminski University)", "Oct 2021", "Jun 2022"), Education("Postgraduate Degree, Data Scientist - Big Data i Systemy zaawansowanej analizy danych", "Akademia WSB - WSB University", "Oct 2020", "May 2021"), Education("Doctorate (Dr), Biology", "Uniwersytet Szczeciński", "2012", "2018"), Education("Postgraduate, Financial management and controlling (in Polish)", "Uniwersytet WSB Szczecin", "2019", "2020"), Education("Master's degree, Biology/Biological Sciences, General", "Uniwersytet Szczeciński", "2006", "2011")]

cv = {
    "contact": contact,
    "summary": summary,
    "experience": experience,
    "skills": skills,
    "education": education
}

markdown_cv = generate_markdown(cv)
