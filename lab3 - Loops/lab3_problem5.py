#Problem 5. Print Fibonacci numbers below a given user input N.

n=int(input("Enter a number : "))
a=0
b=1

while a<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c

print("Fibonacci series : ",a)