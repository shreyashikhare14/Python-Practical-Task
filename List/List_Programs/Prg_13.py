"""
13. Find the index of a specific element using index().
"""

lst1= input("Enter a List = ")
lst = list(map(int,lst1.split()))

print("Original List is = ",lst)

search_element = int(input("Enter a specific element = "))

element_index = lst.index(search_element)

print("Index of Specific Element is = ",element_index)