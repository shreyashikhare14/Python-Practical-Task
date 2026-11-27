"""
2. Create a list of strings and add a new string at the end using append().

"""
str = input("Enter a String = ")
org_lst = str.split()

print("Original String is = ",org_lst)

new_lst= input("Enter a new String = ")

org_lst.append(new_lst)

print("Updated String is = ",org_lst)
