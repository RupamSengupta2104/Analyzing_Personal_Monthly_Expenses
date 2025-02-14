import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the "data" folder exists
os.makedirs("data", exist_ok=True)

# Load the data
data = {
    "Date": ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", 
             "2023-10-06", "2023-10-07", "2023-10-08", "2023-10-09", "2023-10-10",
             "2023-10-11", "2023-10-12", "2023-10-13", "2023-10-14", "2023-10-15",
             "2023-10-16", "2023-10-17", "2023-10-18", "2023-10-19", "2023-10-20",
             "2023-10-21", "2023-10-22", "2023-10-23", "2023-10-24", "2023-10-25",
             "2023-10-26", "2023-10-27", "2023-10-28", "2023-10-29", "2023-10-30", "2023-10-31"],
    "Category": ["Food", "Transportation", "Entertainment", "Food", "Utilities", 
                 "Food", "Transportation", "Entertainment", "Food", "Utilities",
                 "Food", "Transportation", "Entertainment", "Food", "Utilities",
                 "Food", "Transportation", "Entertainment", "Food", "Utilities",
                 "Food", "Transportation", "Entertainment", "Food", "Utilities",
                 "Food", "Transportation", "Entertainment", "Food", "Utilities", "Food"],
    "Description": ["Groceries", "Bus fare", "Movie tickets", "Restaurant", "Electricity bill",
                    "Groceries", "Taxi", "Concert tickets", "Restaurant", "Internet bill",
                    "Groceries", "Train fare", "Netflix subscription", "Restaurant", "Water bill",
                    "Groceries", "Bus fare", "Movie tickets", "Restaurant", "Gas bill",
                    "Groceries", "Taxi", "Concert tickets", "Restaurant", "Electricity bill",
                    "Groceries", "Train fare", "Netflix subscription", "Restaurant", "Internet bill", "Groceries"],
    "Amount": [50, 5, 20, 30, 100, 40, 15, 50, 25, 40, 
               60, 10, 15, 35, 50, 45, 5, 25, 40, 70, 
               55, 20, 60, 30, 100, 50, 10, 15, 40, 40, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add a Month column
df["Month"] = "October"

# Display the first few rows
print(df.head())
'''
# Ensure the "images" folder exists
os.makedirs("images", exist_ok=True)

# Load the data
df = pd.read_csv(csv_path)

# Group by category and sum expenses
category_expenses = df.groupby("Category")["Amount"].sum()

# Plot a bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x=category_expenses.index, y=category_expenses.values, palette="viridis")
plt.xlabel("Category")
plt.ylabel("Total Expenses")
plt.title("Total Expenses by Category")
plt.xticks(rotation=45)

# Save the figure
image_path = "images/expenses_by_category.png"
plt.savefig(image_path)
print(f"Visualization saved to {image_path}")

# Show the plot
plt.show()
'''