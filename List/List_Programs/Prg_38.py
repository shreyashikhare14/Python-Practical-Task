"""
38. Create a list and count total elements.
"""

lst1 = input("Enter a list of elements = ")
lst = list(map(int,lst1.split()))

print(len(lst))