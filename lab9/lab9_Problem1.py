import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
s = pd.Series(calories)

print("Summation:", s.sum())