"""
42. Calculate sum of squares of first n numbers.
"""
n=int(input("Enter a number ="))

total = 0

for i in range(1,n +1):
    total = total +(i*i)
print("Sum of Squares = ",total)