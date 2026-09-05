import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lab10/iris.csv")

# Line plot
plt.plot(df["SepalLengthCm"])
plt.show()

# Scatter plot
plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"])
plt.show()

# Bar chart
plt.bar(df["Species"].value_counts().index,
        df["Species"].value_counts().values)
plt.show()

# Histogram
plt.hist(df["SepalLengthCm"])
plt.show()

# Pie chart
df["Species"].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()

# Subplots
fig, ax = plt.subplots(1, 2)
ax[0].hist(df["SepalLengthCm"])
ax[1].scatter(df["SepalLengthCm"], df["SepalWidthCm"])
plt.show()