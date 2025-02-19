import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Create a synthetic dataset
data = {
    "Year": [2018, 2019, 2020, 2021, 2022, 2023],
    "Country": ["USA", "USA", "USA", "USA", "USA", "USA"],
    "Unemployment Rate (%)": [3.9, 3.5, 8.1, 5.4, 4.3, 3.8],
    "GDP Growth Rate (%)": [2.9, 2.3, -3.4, 5.7, 2.1, 3.0],
    "COVID Impact": [0, 0, 1, 0, 0, 0]  
}
# 1 means COVID impacted the unemployment rate


# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('unemployment_analysis.csv', index=False)

# Display the first few rows of the dataset
print(df)


# Step 1: Load the dataset from the CSV file
df = pd.read_csv('unemployment_analysis.csv')

# Step 2: Basic Exploratory Data Analysis (EDA)
# Show the first few rows of the dataset
print("Dataset Overview:")
print(df.head())

# Show summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Visualize the Unemployment Rate over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Unemployment Rate (%)', marker='o', color='blue')
plt.title('Unemployment Rate Over the Years (USA)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()

# Step 4: Visualize the relationship between GDP Growth Rate and Unemployment Rate
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='GDP Growth Rate (%)', y='Unemployment Rate (%)', hue='COVID Impact', palette='coolwarm', s=100)
plt.title('GDP Growth Rate vs. Unemployment Rate (USA)', fontsize=16)
plt.xlabel('GDP Growth Rate (%)')
plt.ylabel('Unemployment Rate (%)')
plt.legend(title="COVID Impact", loc='best')
plt.grid(True)
plt.show()

# Step 5: Highlight the impact of COVID on Unemployment
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Year', y='Unemployment Rate (%)', hue='COVID Impact', palette='viridis')
plt.title('Impact of COVID on Unemployment Rate (USA)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.legend(title="COVID Impact", loc='best')
plt.grid(True)
plt.show()

# Step 6: Calculate the correlation between GDP Growth Rate and Unemployment Rate
correlation = df[['GDP Growth Rate (%)', 'Unemployment Rate (%)']].corr()
print("\nCorrelation between GDP Growth Rate and Unemployment Rate:")
print(correlation)

# Step 7: Analyzing the Unemployment rate during COVID (2020)
covid_impact_df = df[df['COVID Impact'] == 1]
print("\nUnemployment Rate During COVID (2020):")
print(covid_impact_df[['Year', 'Unemployment Rate (%)', 'GDP Growth Rate (%)']])

# Step 8: Trend analysis for Unemployment Rate from 2018 to 2023
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Year', y='Unemployment Rate (%)', hue='COVID Impact', palette='Set2', marker='o', linewidth=2)
plt.title('Unemployment Rate Trend from 2018 to 2023 (USA)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()
