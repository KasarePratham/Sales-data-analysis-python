#importing Liabraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading Dataset csv file
df = pd.read_csv("Superstore.csv",encoding='latin1')

#converting date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

#removing Null Values
df = df.dropna()

#Printing Total Sales
total_sales = df['Sales'].sum()
print("Total_sales :",(total_sales))

#Searching top 5 Products sold
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Products :\n", top_products)

# Getting Month wise sale
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()

#Calculating profits
profit = df.groupby('Category')['Profit'].sum()

#Making Gragh of analysis
monthly_sales.plot(kind='bar')

#plt.title("Monthly Sales Trend")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

top_products.plot(kind='bar')
plt.title("Sales by top 5 category")

plt.xlabel("Category")
plt.ylabel("Sales")
