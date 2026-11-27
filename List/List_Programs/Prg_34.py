"""
34. Create a list and find common elements between two lists.
"""
lst1 = input("Enter a list First Elements = ")
lst_first = lst1.split()

lst2 = input("Enter a list second Elements = ")
lst_second = lst2.split()

new_lst = []

for i in lst_first:
    if i in lst_second:
        new_lst.append(i)

print(new_lst)
