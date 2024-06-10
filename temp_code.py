import pandas as pd

# Load the example data
df = pd.read_csv('temp_csv.csv')

# Define the rules
rules = [
    ("Higher Age", df['age'].apply(lambda x: x > 20).sum()),  # Assuming 20 is the threshold for 'higher age'
    ("Government Sector Employment", (df['workclass'] == 'Government').sum()),
    ("Higher Education", df['education'].apply(lambda x: x in ['Doctorate', 'Prof-school']).sum()),
    ("Married Status", (df['marital_status'] == 'Married').sum()),
    ("Professional Occupation", df['occupation'].apply(lambda x: x in ['Professional', 'Sales']).sum())
]

# Create the DataFrame
df_final = pd.DataFrame(rules, columns=['Rule', 'Importance'])

# Check if the example follows the rules
df_final['In explanation'] = [
    int(df['age'].iloc[0] > 20),  # Check if age is higher
    int(df['workclass'].iloc[0] == 'Government'),  # Check if workclass is Government
    int(df['education'].iloc[0] in ['Doctorate', 'Prof-school']),  # Check if education is higher
    int(df['marital_status'].iloc[0] == 'Married'),  # Check if marital status is Married
    int(df['occupation'].iloc[0] in ['Professional', 'Sales'])  # Check if occupation is Professional or Sales
]

# Save to csv
df_final.to_csv('evaluation.csv', index=False)