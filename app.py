from flask import Flask, render_template, request, send_file
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for Flask
import matplotlib.pyplot as plt
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # This now renders landing.html instead of index.html for the Tax Compliance System
    return render_template('landing.html') 

@app.route('/input')
def input_page():
    # This route serves the input form page for the Tax Compliance System
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        df = pd.read_csv('inputfiles/personal_transactions.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        df = df[df['Transaction Type'].str.lower() == 'debit']

        num_transactions = int(request.form['days'])

        if num_transactions > len(df):
            return f"Only {len(df)} transactions available. Please enter a smaller number."

        new_rows_df = df.head(num_transactions).copy().sort_values(by='Date')
        new_rows_df['Tax Amount'] = new_rows_df['Amount'] * 0.10
        new_rows_df['Non-Tax Amount'] = new_rows_df['Amount'] * 0.90
        new_rows_df = new_rows_df[['Date', 'Amount', 'Tax Amount', 'Non-Tax Amount']]

        output_folder = 'output'
        os.makedirs(output_folder, exist_ok=True)
        excel_path = os.path.join(output_folder, 'extracted_data.xlsx')

        # ✅ Append to existing Excel file if it exists
        if os.path.exists(excel_path):
            existing_df = pd.read_excel(excel_path)
            combined_df = pd.concat([existing_df, new_rows_df], ignore_index=True)
        else:
            combined_df = new_rows_df

        combined_df.to_excel(excel_path, index=False)

        # Save EDA results
        eda_results = []
        eda_results.append("Summary Statistics:\n")
        eda_results.append(df.describe().to_string())
        eda_results.append("\n\nMissing Values:\n")
        eda_results.append(df.isnull().sum().to_string())
        eda_results.append("\n\nData Types:\n")
        eda_results.append(df.dtypes.to_string())
        eda_results.append("\n\nTop Categories by Frequency:\n")
        eda_results.append(df['Category'].value_counts().to_string())
        eda_results.append("\n\nTop Categories by Amount:\n")
        eda_results.append(df.groupby('Category')['Amount'].sum().sort_values(ascending=False).to_string())

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        eda_path = os.path.join(output_folder, f'eda_results_{timestamp}.txt')
        with open(eda_path, 'w') as f:
            f.write("\n".join(eda_results))

        transactions = new_rows_df.to_dict(orient='records')

        plt.figure(figsize=(10, 6), facecolor='white') # Added facecolor to explicitly set background
        plt.plot(new_rows_df['Date'], new_rows_df['Tax Amount'], marker='o')
        plt.title('Tax Amount Over Time')
        plt.xlabel('Date')
        plt.ylabel('Tax Amount')
        plt.grid(True)
        plt.tight_layout() # Added for better plot layout
        graph_path = 'static/graph.png'
        plt.savefig(graph_path)
        plt.close()

        return render_template('result.html', transactions=transactions, graph_url='/' + graph_path, excel_url='/download_excel')

    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"An unexpected error occurred: {e}"

@app.route('/download_excel')
def download_excel():
    return send_file('output/extracted_data.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)