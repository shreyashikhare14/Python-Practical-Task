"""
6. Remove an element from a specific index using pop(index).
"""

lst1 = input("Enter a List = ")
lst = lst1.split()

print("Original List is = ",lst)

index = int(input("Enter a index to remove = "))
lst.pop(index)

print("Updated List is = ",lst)