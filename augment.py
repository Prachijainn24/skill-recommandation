import pandas as pd
import random

df = pd.read_csv("companies.csv")
df.columns = df.columns.str.strip()

# ---------------- AUGMENTATION ---------------- #

skill_map = {
    "Java": ["Core Java", "Java SE"],
    "Python": ["Python3", "Python Programming"],
    "SQL": ["MySQL", "PostgreSQL"],
    "React": ["ReactJS"],
    "Node": ["Node.js"]
}

locations = ["Mumbai", "Pune", "Bangalore", "Hyderabad", "Chennai"]

augmented_data = []

for _, row in df.iterrows():
    for i in range(2):

        skills = str(row["tools_and_technologies"]).split(",")
        new_skills = []

        for skill in skills:
            skill = skill.strip()
            if skill in skill_map:
                new_skills.append(random.choice(skill_map[skill]))
            else:
                new_skills.append(skill)

        new_row = {
            "company_id": random.randint(1000, 9999),
            "company_name": row["company_name"],
            "industry_domain": row["industry_domain"],
            "salary": round(float(row["salary"]) + random.uniform(-1, 2), 1),
            "location": random.choice(locations),
            "tools_and_technologies": ",".join(new_skills),
            "role_name": row["role_name"],
            "role_category": row["role_category"],
            "experience_level": random.choice(["Entry", "Mid"])
        }

        augmented_data.append(new_row)

aug_df = pd.DataFrame(augmented_data)

final_df = pd.concat([df, aug_df], ignore_index=True)

final_df.to_csv("final_companies_dataset.csv", index=False)

print("🔥 DONE! Clean + augmented dataset ready")