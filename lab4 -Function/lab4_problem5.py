#Problem 5. Write a Python function that will take a list and print the counts of all distinct elements. Sample List : [10,20,30,30,30,30,20,40] Sample output : 10 => 1, 20 => 2, 30 => 4, 40 => 1

def count_elements(lst):
    for i in set(lst):
        print(i, "=>", lst.count(i))

lst = [10,20,30,30,30,30,20,40]
count_elements(lst)