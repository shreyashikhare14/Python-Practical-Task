"""
44. Print alternate characters of a string.
"""
str = input("Enter a String =")

for i in range (0,len(str),2):
    print(str[i],end="")
