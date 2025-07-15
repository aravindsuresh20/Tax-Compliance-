# Tax-Compliance-

# 💰 Personal Transaction Analysis and Tax Compliance System

This project provides a web-based application built with **Flask** and **Python** for analyzing personal financial transactions, specifically focusing on **debit transactions** to calculate potential **tax (10%)** and **non-tax (90%)** amounts. It includes data extraction, **Exploratory Data Analysis (EDA)**, dynamic visualizations, and a **Linear Regression model** for predicting future transaction amounts.

---

## 🚀 Features

- **🌐 Web-Based Interface**  
  A user-friendly Flask application for interacting with the system.

- **🔍 Transaction Processing**  
  Filters debit transactions from a CSV file to calculate:
  - **Tax Amount (10%)**
  - **Non-Tax Amount (90%)**

- **📤 Data Extraction & Logging**  
  Saves processed transactions to `extracted_data.xlsx` for history tracking.

- **📊 Exploratory Data Analysis (EDA)**  
  Automatically generates a detailed EDA report (`eda_results_*.txt`) with:
  - Summary statistics
  - Missing values
  - Data types
  - Top categories by frequency and amount

- **📈 Dynamic Graph Generation**  
  Visualizes **Tax Amount Over Time** and saves it as `graph.png`.

- **🧠 Model Training**  
  Uses **Linear Regression** to predict transaction amounts based on day count and saves the model as `model.pkl`.

- **📥 Report Download**  
  Users can download the Excel log from the web interface.

---

## 🧰 Requirements

Make sure the following Python libraries are installed:

- `Flask` – for the web framework  
- `pandas` – for data manipulation  
- `matplotlib` – for plotting  
- `scikit-learn` – for machine learning  
- `pickle` – for saving/loading models  
- `openpyxl` – for Excel file support  

Install all using:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
/your-project-directory/
│── app.py                                # Flask web application
│── model.py                              # Linear Regression model training
│── requirements.txt                      # Python dependencies
│── README.md                             # Documentation
│
├── /inputfiles/
│   └── personal_transactions.csv         # Input dataset
│
├── /output/
│   ├── extracted_data.xlsx               # Processed transaction log
│   └── eda_results_YYYYMMDD_HHMMSS.txt   # EDA report
│
├── /static/
│   └── graph.png                         # Tax Over Time graph
│
├── /templates/
│   ├── landing.html                      # Home page
│   ├── input.html                        # User input page
│   └── result.html                       # Results and download page
│
└── model.pkl                             # Trained regression model
```

---

## ⚙️ Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/personal-transaction-analysis.git
cd personal-transaction-analysis
```

2. **Add Dataset**  
Place `personal_transactions.csv` inside the `/inputfiles/` directory. Ensure the file contains:
- `Date`
- `Amount`
- `Transaction Type`
- `Category`

3. **Create `requirements.txt`**

```txt
Flask
pandas
matplotlib
scikit-learn
openpyxl
```

4. **(Optional) Create Virtual Environment**

```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

5. **Install Dependencies**

```bash
pip install -r requirements.txt
```

6. **Train the Regression Model**

```bash
python model.py
```

This creates `model.pkl` in the project root.

7. **Run the Flask App**

```bash
python app.py
```

8. **Open in Browser**

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧑‍💻 Usage

- **Model Training:**  
  Run `model.py` first to generate the prediction model (`model.pkl`).

- **System Deployment:**  
  Start the Flask server by running `app.py`.

- **Input Parameters:**  
  Use the web interface to input the number of transaction days to analyze.

- **View Results & Insights:**  
  On submission:
  - See processed debit transactions
  - View tax/non-tax split
  - Get dynamic tax graph over time
  - Optionally download the Excel log

---

## 📂 Output Files

- **`output/extracted_data.xlsx`**  
  Log of all processed transactions (can be downloaded from the app).

- **`output/eda_results_*.txt`**  
  Summary statistics and insights on the uploaded dataset.

- **`static/graph.png`**  
  Visualization of Tax Amount Over Time.

---

