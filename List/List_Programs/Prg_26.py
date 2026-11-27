"""
26. Create two lists and merge them into one.
"""

lst1 = input("Enter a List1 = ")
lst = list(map(int,lst1.split()))

lst2= input("Enter a List 2nd = ")
lst_second = list(map(int,lst2.split()))

lst3 = lst + lst_second 

print(lst3)