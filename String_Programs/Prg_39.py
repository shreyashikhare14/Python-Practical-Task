"""
39. Check whether a string is a valid identifier.
"""

string = input("Enter a String = ")

if string.isidentifier():
    print("Valid Identifier.")
else:
    print("Invalid Identifier.")