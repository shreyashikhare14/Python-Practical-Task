"""
 Calculate factorial of a number using for loop.

"""

num = int(input("Enter a number = "))
fact  = 1

for i in range(1,num + 1) :
    fact =  i * fact 
print("Factorial is =",fact)
