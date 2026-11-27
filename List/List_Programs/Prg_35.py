"""
35. Create a list and remove all even numbers.
"""

lst1 = input("Enter a List of elements = ")
lst = list(map(int,lst1.split()))

new_lst = []

for i in lst :
    if i % 2 != 0 :
        new_lst.append(i)

print(new_lst)