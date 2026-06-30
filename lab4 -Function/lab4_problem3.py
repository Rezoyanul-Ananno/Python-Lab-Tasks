#Problem 3. Write a Python function that checks whether a passed string is a palindrome. 

def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome("madam")