"""
26. Find the first and last occurrence of a character.
"""

string =input("Enter a String =")
char = input("Enter a Character = ")

first = string.find(char)
last = string.rfind(char)

if first != -1:
    print("First Occurence is = ",first)
    print("Last Occurence is = ",last)
else:
    print("Character Not Found ")