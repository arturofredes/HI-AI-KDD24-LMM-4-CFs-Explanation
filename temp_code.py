import pandas as pd

# Load the provided example
df = pd.read_csv('temp_csv.csv')

# Define the rules and their importance from each system
rules = [
    {"Rule": "Age Rule: Individuals around the age of 62 and 75 are more likely to earn more than $50k.", "Importance": 2},
    {"Rule": "Workclass Rule: Being 'Self-Employed' increases the likelihood of earning more than $50k.", "Importance": 2},
    {"Rule": "Education Rule: Having a 'Doctorate' or 'Masters' degree, or even 'Some-college' education, positively influences income.", "Importance": 5},
    {"Rule": "Occupation Rule: Working in the 'Service' sector can result in earning more than $50k.", "Importance": 1},
    {"Rule": "Race Rule: Being of a race other than 'White' can positively impact income prediction.", "Importance": 3},
    {"Rule": "Rule 1: Higher Education Level", "Importance": 3},
    {"Rule": "Rule 2: Change in Workclass", "Importance": 1},
    {"Rule": "Rule 3: Change in Occupation", "Importance": 1},
    {"Rule": "Rule 4: Increased Working Hours", "Importance": 1},
    {"Rule": "Rule 5: Racial Factor", "Importance": 2},
    {"Rule": "Rule 6: Age Consideration", "Importance": 1},
    {"Rule": "Race", "Importance": 2},
    {"Rule": "Workclass", "Importance": 2},
    {"Rule": "Education Level", "Importance": 3},
    {"Rule": "Gender", "Importance": 1},
    {"Rule": "Hours Per Week", "Importance": 1},
]

# Function to check if rule is followed
def rule_followed(rule, df):
    if "Age Rule" in rule:
        return 1 if df['age'].values[0] in [62, 75] else 0
    if "Workclass Rule" in rule:
        return 1 if df['workclass'].values[0] == "Self-Employed" else 0
    if "Education Rule" in rule:
        return 1 if df['education'].values[0] in ["Doctorate", "Masters", "Some-college"] else 0
    if "Occupation Rule" in rule:
        return 1 if df['occupation'].values[0] == "Service" else 0
    if "Race Rule" in rule or "Racial Factor" in rule or "Race" in rule:
        return 1 if df['race'].values[0] != "White" else 0
    if "Rule 1" in rule:
        return 1 if df['education'].values[0] in ["Prof-school", "Bachelors"] else 0
    if "Rule 2" in rule or "Workclass" in rule:
        return 1 if df['workclass'].values[0] == "Government" else 0
    if "Rule 3" in rule:
        return 1 if df['occupation'].values[0] == "Sales" else 0
    if "Rule 4" in rule or "Hours Per Week" in rule:
        return 1 if df['hours_per_week'].values[0] > 40 else 0
    if "Rule 5" in rule:
        return 1 if df['race'].values[0] != "White" else 0
    if "Rule 6" in rule:
        return 1 if df['age'].values[0] < 50 else 0
    if "Gender" in rule:
        return 1 if df['gender'].values[0] == "Female" else 0
    return 0

# Apply the rule check function
for rule in rules:
    rule["In explanation"] = rule_followed(rule["Rule"], df)

# Create a DataFrame from the rules
df_final = pd.DataFrame(rules)

# Save to csv
df_final.to_csv('evaluation.csv', index=False)