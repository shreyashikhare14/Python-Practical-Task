"""
36. Create a list and remove all odd numbers.
"""
lst1 = input("Enter a List of Elements = ")
lst = list(map(int,lst1.split()))

new_lst = []

for i in lst :
    if i % 2 == 0:
        new_lst.append(i)

print("After Removing Odd Numbers  = ",new_lst)