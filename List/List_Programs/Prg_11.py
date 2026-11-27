"""
11. Sort a list of numbers in descending order using sort(reverse=True).
"""

lst1 = input("Enter a List = ")
lst = list(map(int,lst1.split()))

print("Original List = ",lst)

lst.sort(reverse=True)

print("Descending order List = ",lst)