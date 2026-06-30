#Problem 2. Write a Python program that checks whether a string is a palindrome. 
#Note: A palindrome is a word, number, phrase, or other sequence of symbols that reads the same 
#backwards as forwards, such as madam or racecar.

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")