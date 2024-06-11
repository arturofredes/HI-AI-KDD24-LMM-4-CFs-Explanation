import pandas as pd

# Load the example
df_example = pd.read_csv('temp_csv.csv')

# Define the rules
rules = [
    {"rule": "Higher education levels (Masters, Bachelors)", "importance": 2, "condition": lambda row: row['education'] in ['Masters', 'Bachelors']},
    {"rule": "Being employed in the Government workclass", "importance": 1, "condition": lambda row: row['workclass'] == 'Government'},
    {"rule": "Complex relationship between hours worked and income", "importance": 1, "condition": lambda row: row['hours_per_week'] != 40},
    {"rule": "Race other than White", "importance": 3, "condition": lambda row: row['race'] != 'White'},
    {"rule": "Specific occupations (like Service)", "importance": 1, "condition": lambda row: row['occupation'] == 'Service'},
    {"rule": "Being 'Self-Employed' or working in certain occupations like 'White-Collar' or 'Sales'", "importance": 3, "condition": lambda row: row['workclass'] == 'Self-Employed' or row['occupation'] in ['White-Collar', 'Sales']},
    {"rule": "Age alone is not a significant determining factor", "importance": 5, "condition": lambda row: True}, # Age rule is not clear, hence always True
    {"rule": "Race does not seem to be a critical factor", "importance": 5, "condition": lambda row: True}, # Race rule is not clear, hence always True
    {"rule": "Change in Race", "importance": 2, "condition": lambda row: row['race'] != 'White'},
    {"rule": "Education Level", "importance": 3, "condition": lambda row: row['education'] in ['Bachelors', 'Doctorate']},
    {"rule": "Workclass", "importance": 3, "condition": lambda row: row['workclass'] in ['Self-Employed', 'Government', 'Private']},
    {"rule": "Hours per Week", "importance": 5, "condition": lambda row: row['hours_per_week'] != 40},
]

# Check if the example follows each rule
results = []
for rule in rules:
    is_followed = int(rule['condition'](df_example.iloc[0]))
    results.append({"Rule": rule["rule"], "Importance": rule["importance"], "In explanation": is_followed})

# Create a DataFrame with the results
df_final = pd.DataFrame(results)

# Save to csv
df_final.to_csv('evaluation.csv', index=False)