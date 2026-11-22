""""
31. Remove punctuation marks from a string.
"""

string = input("Enter a String = ")
punctuation = ".,!?;:'\"()-"    
new_string =""

for i in string:
    if i not in punctuation:
        new_string = new_string + i

print("String Without Punctuations marks is =",new_string)