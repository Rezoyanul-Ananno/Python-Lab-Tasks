import pandas as pd

df = pd.read_csv("titanic9.csv")

# Empty cells
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Wrong format
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Wrong data
df = df[df["Age"] >= 0]

# Duplicates
df = df.drop_duplicates()

print(df.head())