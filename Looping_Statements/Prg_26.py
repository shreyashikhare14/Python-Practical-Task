"""
26. Print ASCII values of characters in a string.
"""
str = input("Enter a String = ")

for i in str :
    ascci_val = ord(i)
    print(i,"=",ascci_val)