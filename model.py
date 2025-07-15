import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression

# Define the input file name
input_file = 'C:/Users/AS5560/Downloads/tax compilance/inputfiles/personal_transactions.csv'

# Check if the file exists
if not os.path.exists(input_file):
    raise FileNotFoundError(f"❌ The file '{input_file}' was not found. Please make sure it exists in the specified path.")

# Load the dataset (CSV instead of Excel)
df = pd.read_csv(input_file)

# Filter for debit transactions
df = df[df['Transaction Type'].str.lower() == 'debit']

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by Date and sum the Amount
daily = df.groupby('Date').sum(numeric_only=True).reset_index()

# Calculate the number of days since the start of the dataset
daily['Days'] = (daily['Date'] - daily['Date'].min()).dt.days

# Prepare the features (X) and target (y)
X = daily[['Days']]
y = daily['Amount']

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model to a pickle file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model has been trained and saved as 'model.pkl'")
