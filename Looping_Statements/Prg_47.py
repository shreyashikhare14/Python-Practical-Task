"""
47. Find product of digits of a number.
"""
num = int(input("Enter a number = "))
product=1

while num > 0:
    digit = num % 10 
    product = product * digit
    num = num // 10 
print("Product of Digits is = ",product)

# Product means multiplication of number of each digit like 134 = 1 * 3 * 4 = 12