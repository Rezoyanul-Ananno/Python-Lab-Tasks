#Problem 1.  Write a Python program to reverse all words in a string.  Sample string: 'hello .py' Expected Result: 'olleh yp.'

s = 'hello .py'

words = s.split()
result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))