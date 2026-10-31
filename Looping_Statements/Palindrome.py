"""
13. Check whether a number is palindrome.
"""
num = int(input("Enter a number ="))
print(num)
original = num
reverse = 0
while num >0:
    digits = num % 10
    reverse = reverse * 10 + digits
    num = num // 10 

if original == reverse:
    print("Palindrome ")
else:
    print("Not Palindrome")

