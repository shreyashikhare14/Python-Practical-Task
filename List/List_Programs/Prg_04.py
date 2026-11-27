"""
4. Create a list and remove a specific element using remove().
"""

user_lst = input("Enter a list = ")

lst = user_lst.split()

remove_lst = input("Enter a specific elemnet for remove = ")

lst.remove(remove_lst)

print("Updated List = ",lst)
