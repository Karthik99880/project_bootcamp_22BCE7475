import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read in your sovereign bonds datase

url = 'https://www.kaggle.com/datasets/stefanoleone992/mutual-funds-and-etfs'
df = pd.read_csv(url)
data = pd.read_csv('your_sovereign_bonds_dataset.csv')

data = data.dropna()

data = data.sort_values(by=['Issuer', 'YTM', 'Duration'])


data['YTM'] = data['Coupon'] / data['Price']

# Calculate the average yield to maturity for each issuer
average_yields = data.groupby('Issuer')['YTM'].mean()

# Calculate the median market cap for each issuer
median_market_caps = data.groupby('Issuer')['Market Cap'].median()

# Calculate the median yield to maturity for each issuer
median_yields = data.groupby('Issuer')['YTM'].median()


issuer_stats = pd.concat([average_yields, median_market_caps, median_yields], axis=1, keys=['Average YTM', 'Median Market Cap', 'Median YTM'])

# Create a scatter plot of yield to maturity vs. duration for each issuer
for issuer in data['Issuer'].unique():
    issuer_data = data[data['Issuer'] == issuer]
    plt.scatter(issuer_data['Duration'], issuer_data['YTM'], label=issuer)

plt.title('Yield to Maturity vs Duration for Each Issuer')
plt.xlabel('Duration')
plt.ylabel('Yield to Maturity')
plt.legend()
plt.show()

# Use a heatmap to visualize the relationship between the variables
correlation_matrix = data.corr()
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Print the stats for each issuer
print(issuer_stats)