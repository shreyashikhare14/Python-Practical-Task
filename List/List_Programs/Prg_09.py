"""
9. Count how many times a specific element appears using count().
"""

lst1 = input("Enter a list = ")
lst = lst1.split()

print("Original List = ",lst)

search_element = input("Enter a element to count = ")

lst.count(search_element)

count_element= lst.count(search_element)
print("Element Count = ",count_element)
