"""
36. Remove duplicate characters from a string.
"""

string = input("Enter a String = ")

result =""

for char in string:
    if char not in result:
        result = result + char

print("String after removing Duplicates = ",result)