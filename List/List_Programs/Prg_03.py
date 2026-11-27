"""
3. Insert an element at the 3rd position using insert().
"""

lst = list(map(int,input("Enter a list = ").split()))

print("Old List = ",lst)

new_lst = int(input("Enter a new element = "))

lst.insert(3,new_lst)

print("Updated List is =",lst)