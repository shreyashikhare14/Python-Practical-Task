"""
5. Print multiplication table of a given number.
"""

num = int(input("Enter Table Number = "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)