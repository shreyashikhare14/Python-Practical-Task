"""
22. Find sum of even digits in a number.
"""
num = int(input("Enter a Number ="))
sum = 0
while num >0:
    digit = num % 10
    if digit % 2 ==0:
        sum = sum + digit
    num = num // 10
print("Sum of Total Even Number is = ",sum)

