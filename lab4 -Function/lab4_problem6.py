#Problem 6. Write a Python lambda function to find if a given string starts with a given sub-string using Lambda.

starts_with = lambda s, sub: s.startswith(sub)

print(starts_with("Python Programming", "Python"))