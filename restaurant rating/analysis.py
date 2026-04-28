import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("zomato.csv")

# Check column names
print(df.columns)

# Distribution of ratings
print(df['Aggregate rating'].describe())

# Plot histogram
plt.hist(df['Aggregate rating'], bins=10)
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.show()

# Create rating ranges
bins = [0,1,2,3,4,5]
labels = ['0-1','1-2','2-3','3-4','4-5']

df['Rating Range'] = pd.cut(df['Aggregate rating'], bins=bins, labels=labels)

# Most common range
print(df['Rating Range'].value_counts())