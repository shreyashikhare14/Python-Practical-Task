"""
30. Create a list of strings and sort alphabetically.
"""

lst1 = input("Enter a List of string = ").strip()
lst = lst1.split()

lst.sort()

print("Alphabetically Sorted List is = ",lst)