"""
21. Find the length of a string without using len().
"""
string = input("Enter a String = ")

count = 0
for i in string:
    count = count + 1 

print("Length of String is = ",count)