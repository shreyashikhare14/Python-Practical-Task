"""
20. Remove all occurrences of a given character from a string.
"""

string = input("Enter a String =")
char = input("Enter character to remove =")

new_string = string.replace(char,"")

print("Original String = ",string)
print("String After removing character = ",new_string)

