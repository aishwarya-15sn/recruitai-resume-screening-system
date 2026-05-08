def extract_skills(text):
    skills_db = ["python", "sql", "machine learning", "fastapi", "nlp"]
    found = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return found
