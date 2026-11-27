"""
31. Create a list of numbers and sort without using sort() (use sorted()).
"""

lst1 = input("Enter a List of elements = ")
lst = list(map(int,lst1.split()))

new_lst = sorted(lst)

print("Original List is = ",lst)
print("Sorted List = ",new_lst)
