"""
8. Copy one list into another using copy().
"""

lst1 = input("Enter a list = ")
lst = lst1.split()

print("Original List is = ",lst)

lst_new = lst.copy()

print("Copied List = ",lst_new)