import pandas as pd

# Load the example data
df = pd.read_csv('temp_csv.csv')

# Define the rules and their importance
rules = {
    "Education Level": df['education'].isin(['Bachelors', 'Masters', 'Doctorate', 'Prof-school']).sum(),
    "Occupation": df['occupation'].isin(['Professional', 'Sales', 'Service', 'White-Collar']).sum(),
    "Gender": df['gender'].isin(['Male']).sum(),
    "Work Hours": (df['hours_per_week'] > 40).sum(),
    "Marital Status": df['marital_status'].isin(['Married']).sum(),
    "Race": df['race'].isin(['White']).sum()
}

# Check if the example follows the rules
example = df.iloc[0]
follows_rules = {
    "Education Level": int(example['education'] in ['Bachelors', 'Masters', 'Doctorate', 'Prof-school']),
    "Occupation": int(example['occupation'] in ['Professional', 'Sales', 'Service', 'White-Collar']),
    "Gender": int(example['gender'] == 'Male'),
    "Work Hours": int(example['hours_per_week'] > 40),
    "Marital Status": int(example['marital_status'] == 'Married'),
    "Race": int(example['race'] == 'White')
}

# Create the result DataFrame
df_final = pd.DataFrame({
    'Rule': list(rules.keys()),
    'Importance': list(rules.values()),
    'In explanation': list(follows_rules.values())
})

# Save to csv
df_final.to_csv('evaluation.csv', index=False)