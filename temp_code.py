import pandas as pd

# Read example
df = pd.read_csv('temp_csv.csv')

# Define the rules and their importance
rules = [
    {
        'Rule': 'Being married or divorced increases the likelihood of earning more than $50k.',
        'Importance': 5,
        'Condition': lambda row: row['marital_status'] in ['Married', 'Divorced']
    },
    {
        'Rule': 'Professional occupations have a higher likelihood of leading to higher income compared to service occupations.',
        'Importance': 3,
        'Condition': lambda row: row['occupation'] == 'Professional'
    },
    {
        'Rule': 'Being male increases the likelihood of earning more than $50k.',
        'Importance': 2,
        'Condition': lambda row: row['gender'] == 'Male'
    },
    {
        'Rule': 'Higher levels of education (Associates, Masters) are associated with higher income.',
        'Importance': 2,
        'Condition': lambda row: row['education'] in ['Assoc', 'Masters']
    },
    {
        'Rule': 'Working significantly more hours per week (e.g., 76 hours) increases the likelihood of earning a higher income.',
        'Importance': 1,
        'Condition': lambda row: row['hours_per_week'] >= 76
    }
]

# Initialize the results list
results = []

# Check each rule
for rule in rules:
    is_followed = 1 if rule['Condition'](df.iloc[0]) else 0
    results.append({
        'Rule': rule['Rule'],
        'Importance': rule['Importance'],
        'In explanation': is_followed
    })

# Create the DataFrame
df_final = pd.DataFrame(results)

# Save to csv
df_final.to_csv('evaluation.csv', index=False)