"""
11. Count how many times a particular character appears in a string.
"""

str_name = input("Enter a String =")
for i in str_name :
    count = str_name.count(i)
    print(i,"=",count)