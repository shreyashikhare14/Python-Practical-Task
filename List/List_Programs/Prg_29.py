"""
29. Create a list and delete an element using del keyword.
"""

lst1 =input("Enter a List elments = ")
lst = lst1.split()

ele = input("Enter a element index to remove = ")

del lst[ele]

print("Updated List is = ",lst)