"""
17. Find largest digit in a number.

"""

num = int(input("Enter a Number = "))
largest = 0
while num >0:
    digit  = num % 10 

    if digit > largest :
        largest = digit
    num = num //10  
print("Largest Number is = ",largest)
