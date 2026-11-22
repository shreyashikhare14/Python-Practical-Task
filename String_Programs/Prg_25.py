"""
25. Extract only alphabets from a string.
"""

string = input("Enter a String = ")

alph =""

for i in string :
    if i.isalpha():
        alph = alph + i

print("Extracted Alphabets is = ",alph)