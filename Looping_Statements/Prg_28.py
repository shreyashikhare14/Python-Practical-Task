"""
28. Check whether a number is Armstrong.
"""


num = int(input("Enter a number = "))

temp = num
count = 0
power = len(str(num))

while num > 0 :
    digit = num % 10
    count = count + digit ** power
    num = num // 10 

if count == temp :
    print("Armstrong Number")
else:
    print("Not Armstrong Number")