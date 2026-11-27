"""
12. Reverse the elements of a list using reverse().
"""

lst1 = input("Enter a List = ")
lst = list(map(int,lst1.split()))

print("Original List = ",lst)

lst.reverse()

print("Reverse List is = ",lst)