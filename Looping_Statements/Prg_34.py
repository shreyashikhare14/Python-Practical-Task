"""
34. Check whether a string is palindrome.
"""

str = input("Enter a String = ")
rev = ""

for i in str:
    rev = i + rev

if str == rev:
    print(str, "is Palindrome")
else:
    print(str, "is Not Palindrome")