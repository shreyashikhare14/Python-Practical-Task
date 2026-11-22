"""
23. Check whether a string is a palindrome.
"""

string = input("Enter a String = ")

string=string.lower()
rev_str = string[::-1]

if rev_str == string :
    print("String is Palindrome")
else:
    print("String is not Palindrome")