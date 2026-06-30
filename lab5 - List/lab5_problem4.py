#Problem 4. Write a Python Program to find a specific value from a list of values. [Use linear or binary search]  

numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Not Found")