#Problem 7. Write a Python program to count the number of strings from a given list of strings. 
#The string length is 2 or more and the first and last characters are the same. 
#Sample List : ['aca', 'xyz', 'aba', '1221'] Expected Result : 3

lst = ['aca', 'xyz', 'aba', '1221']

count = 0

for s in lst:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print(count)