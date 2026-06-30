#Problem 4. Write a Python function that takes a list and returns a new list with distinct elements 
#from the list. Sample List : [1,2,3,3,3,3,4,5] Sample output : [1, 2, 3, 4, 5] 

def distinct(lst):
    return list(set(lst))

lst = [1,2,3,3,3,3,4,5]
print(distinct(lst))