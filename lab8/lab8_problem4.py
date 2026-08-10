import pandas as pd

df = pd.read_csv("lab8/titanic.csv")

print("Original Data:")
print(df.head())

# Empty cells
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Wrong format
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Wrong data
df = df[(df["Age"] >= 0) & (df["Age"] <= 100)]

# Duplicates
df.drop_duplicates(inplace=True)

print("\nCleaned Data:")
print(df.head())

print("\nData Information:")
df.info()