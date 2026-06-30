#Problem 2. Write a program to compute the distance between two points, taking input from the user. [Distance formula = d=√((x2-x1)²+(y2-y1)²)]  

a=float(input("Enter X1 : "))
b=float(input("Enter X2 : "))
c=float(input("Enter Y1 : "))
d=float(input("Enter Y2 : "))

distance=((((b-a)**2)+((d-c)**2))**0.5)

print("Distance Between Two point is: ",distance)