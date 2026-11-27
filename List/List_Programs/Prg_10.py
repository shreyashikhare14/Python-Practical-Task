"""
10. Sort a list of numbers in ascending order using sort().
"""

lst1 = input("Enter a List = ")
lst = list(map(int,lst1.split()))

print("Original List = ",lst)

lst.sort()

print("Sorted List = ",lst)