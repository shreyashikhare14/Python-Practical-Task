"""
37. Print numbers until user enters a negative number.
"""

while True :
    num= int(input("Enter a Number ="))

    if num < 0:
        break

    print(num)
