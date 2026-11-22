"""
24. Extract only digits from a string.
"""

string = input("Enter a String = ")
digits = ""

for i in string:
    if i.isdigit():
        digits = digits + i

print("Extracted Digits = ",digits)