required_skills = ["Python", "SQL", "Excel", "COBOL", "Tableau", "VBA"]
applicant_skills = ["Python", "SQL", "PowerBI"]
outdated_string = "COBOL, VBA, Fortran"

required_set = set(required_skills)
applicant_set = set(applicant_skills)
outdated_set = {skill.strip() for skill in outdated_string.split(",")}


modern_requirements = required_set - outdated_set
missing_skills = modern_requirements - applicant_set

print(f"Modern Job Requirements: {modern_requirements}")
print(f"Skills Applicant Lacks: {missing_skills}")