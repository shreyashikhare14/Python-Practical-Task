"""
34. Find the ASCII value of each character in a string.
"""

string = input("Enter a String = ")

for char in string:
    print(char,"=",ord(char))
