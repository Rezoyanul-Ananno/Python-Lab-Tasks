#Problem 5. You have been given a Python list. Write a program to find value 20 in the list, and if 
#it is present, replace it with 200. Update all occurrences of the item. Use loop to access values of 
#the list and do not use replace() function. Sample List: [10, 20, 30, 20, 50] Expected Result: [10, 200, 30, 200, 50]

lst = [10, 20, 30, 20, 50]

for i in range(len(lst)):
    if lst[i] == 20:
        lst[i] = 200

print(lst)
