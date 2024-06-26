import pandas as pd

# Load the CSV file
data_path = 'TFWS.csv'
data = pd.read_csv(data_path, skiprows=1)

# Rename and clean the columns
data.columns = ['INSTITUTE_NAME', 'BRANCH', 'CATEGORY', 'TYPE', 'OPENING', 'CLOSING']
data = data[['INSTITUTE_NAME', 'BRANCH', 'CATEGORY', 'TYPE', 'OPENING', 'CLOSING']].dropna().reset_index(drop=True)

# Ensure ranks are integers
data['OPENING'] = data['OPENING'].astype(int)
data['CLOSING'] = data['CLOSING'].astype(int)

# Save to JSON
output_path = 'TFWS.json'
data.to_json(output_path, orient='records')

data.head()
