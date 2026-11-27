"""
15. Create a list and check membership using in keyword.
"""

lst1 = input("Enter a list = ")
lst = lst1.split()

print("Original List = ",lst)

search_element = input("Enter element to search = ")

if search_element in lst :
    print("Element exists in the list.")

else:
    print("Elemet does not exist in the list.")