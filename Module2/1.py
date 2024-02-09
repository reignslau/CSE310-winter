import pandas as pd

# Load the CSV file into a DataFrame
sales_data = pd.read_csv("sales_data.csv")

# Convert the 'Date' column to datetime format
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Extract the month from the 'Date' column and create a new column
sales_data['Month'] = sales_data['Date'].dt.to_period('M')

# Group the data by month and calculate the total revenue for each month
monthly_revenue = sales_data.groupby('Month')['Revenue'].sum()

# Print the results
print("Monthly Revenue:")
print(monthly_revenue)
