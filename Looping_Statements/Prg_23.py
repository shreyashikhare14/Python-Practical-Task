"""
23. Find sum of odd digits in a number.
"""

num = int(input("Enter a Number ="))
odd_count =0
while num >0:
    digit = num % 10
    if digit % 2 != 0:
        odd_count = odd_count + digit
    num = num // 10
print("Sum of Odd Digits  is = ",odd_count)