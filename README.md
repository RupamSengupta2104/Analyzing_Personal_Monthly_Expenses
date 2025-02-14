Analyzing Personal Monthly Expenses

📌 Project Overview

This project aims to analyze personal monthly expenses using Python, Pandas, Matplotlib, and Seaborn. It includes:

Loading expense data from a CSV file.

Performing data analysis and visualization.

Summarizing total expenses by category and month.

Storing results in a structured directory format.

📂 Project Structure

Analyzing_Personal_Monthly_Expenses/
│── venv/                 # Virtual environment (excluded from Git)
│── data/
│   ├── expenses.csv      # Raw expense data (excluded from Git)
│── images/
│   ├── expense_plot.png  # Saved visualizations
│── scripts/
│   ├── analysis.py       # Main script for data processing
│── .gitignore            # Ignore unnecessary files
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation

⚙️ Setup Instructions

1️⃣ Create Project Folder & Virtual Environment

mkdir Analyzing_Personal_Monthly_Expenses
cd Analyzing_Personal_Monthly_Expenses
python -m venv venv

2️⃣ Activate Virtual Environment

Windows (CMD): venv\Scripts\activate

Windows (PowerShell): venv\Scripts\Activate.ps1

Mac/Linux: source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

If requirements.txt is missing, create it:

echo "pandas\nmatplotlib\nseaborn" > requirements.txt

📊 Data Preparation

The dataset consists of daily expense records with the following columns:

Date             Category             Description            Amount

2023-10-01       Food                 Groceries              50

2023-10-02       Transportation       Bus fare               5

2023-10-03       Entertainment        Movie tickets          20

Convert this data into a CSV file:

import pandas as pd

data = {"Date": [...], "Category": [...], "Description": [...], "Amount": [...]}
df = pd.DataFrame(data)
df.to_csv("data/expenses.csv", index=False)

🛠️ Performing Data Analysis

1️⃣ Load and Inspect Data

import pandas as pd
df = pd.read_csv("data/expenses.csv", parse_dates=["Date"])
print(df.info())
print(df.head())

2️⃣ Monthly Expense Summary

df["Month"] = df["Date"].dt.to_period("M")
monthly_expenses = df.groupby("Month")["Amount"].sum()
print(monthly_expenses)

3️⃣ Visualization of Expenses

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
plt.figure(figsize=(10, 5))
sns.barplot(x=df["Category"], y=df["Amount"], estimator=sum)
plt.xticks(rotation=45)
plt.title("Total Expenses by Category")
plt.savefig("images/expense_plot.png")
plt.show()

🛑 Prevent CSV from Being Pushed to Git

Add this to .gitignore:

venv/
data/expenses.csv
__pycache__/

This ensures that sensitive financial data is not uploaded to GitHub.

✅ Summary

Structured directory for better management.

Uses Pandas for data handling.

Matplotlib & Seaborn for visualization.

Saves results and prevents unwanted files from being committed.