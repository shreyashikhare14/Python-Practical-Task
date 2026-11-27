"""
14. Extend a list by adding elements of another list using extend().
"""
lst1 = input("Enter a List1 = ")
lst = lst1.split()

lst2 = input("Enter a list2 = ")
lst3= lst2.split()

print("Original List1 = ",lst)
print("Original List2 = ",lst2)

lst.extend(lst3)

print("Updated List = ",lst)
