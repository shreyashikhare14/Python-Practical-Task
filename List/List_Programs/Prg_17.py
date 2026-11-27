"""
17. Create a list of mixed data types and display them.
"""

lst1 = input("Enter a List = ")
values = lst1.split()

lst = []

for i in values:
    if i.isdigit():
        lst.append(int(i))
    
    elif i.replace('.','',1).isdigit():
        lst.append(float(i))

    elif i == "True":
        lst.append(True)

    elif i == "False":
        lst.append(False)

    else:
        lst.append(i)

print("Mixed Data Type List = ",lst)

for i in lst :
    print(i,type(i))