#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os  # Import os module
import pandas as pd

# Define file path correctly
csv_file_path = os.path.join("C:/Users/gopal/Downloads", "Sales Data.csv")

# Load the dataset
df = pd.read_csv(csv_file_path)

# Display basic information and first few rows
df.info()
print(df.head())



import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
csv_file_path = "C:/Users/gopal/Downloads/Sales Data.csv"
df = pd.read_csv(csv_file_path)

# Drop NaN values
df = df.dropna()

# Convert data types
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])

# Recalculate the Sales column
df['Sales'] = df['Quantity Ordered'] * df['Price Each']

# Extract month from Order Date
df['Month'] = df['Order Date'].dt.month

# Extract hour from Order Date
df['Hour'] = df['Order Date'].dt.hour

# 1. Best month for sales
df_monthly_sales = df.groupby('Month').sum()['Sales']
plt.figure(figsize=(10,5))
plt.bar(df_monthly_sales.index, df_monthly_sales.values)
plt.xlabel('Month')
plt.ylabel('Sales in USD')
plt.title('Total Sales by Month')
plt.show()

# 2. City with the highest sales
df_city_sales = df.groupby('City').sum()['Sales']
plt.figure(figsize=(10,5))
plt.bar(df_city_sales.index, df_city_sales.values)
plt.xlabel('City')
plt.ylabel('Sales in USD')
plt.xticks(rotation=45)
plt.title('Total Sales by City')
plt.show()

# 3. Best time to advertise
df_hourly_sales = df.groupby('Hour').sum()['Sales']
plt.figure(figsize=(10,5))
plt.plot(df_hourly_sales.index, df_hourly_sales.values, marker='o')
plt.xlabel('Hour')
plt.ylabel('Sales in USD')
plt.title('Total Sales by Hour')
plt.grid()
plt.show()

# 4. Products often sold together
from itertools import combinations
from collections import Counter

df_duplicates = df[df.duplicated(subset=['Order ID'], keep=False)]
product_pairs = df_duplicates.groupby('Order ID')['Product'].apply(lambda x: list(combinations(x, 2)))
pair_counts = Counter([pair for pairs in product_pairs for pair in pairs])

# Display top 10 most common pairs
print(pair_counts.most_common(10))

# 5. Best-selling product
df_product_sales = df.groupby('Product').sum()['Quantity Ordered']
plt.figure(figsize=(10,5))
plt.bar(df_product_sales.index, df_product_sales.values)
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=90)
plt.title('Total Quantity Sold by Product')
plt.show()


# In[ ]:




