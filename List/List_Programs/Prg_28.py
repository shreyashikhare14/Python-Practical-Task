"""
28. Create a tuple and convert it into a list.
"""

tup = input("Enter a elements = ")
tup_name = tuple(tup.split())

lst = list(tup_name)

print(lst)