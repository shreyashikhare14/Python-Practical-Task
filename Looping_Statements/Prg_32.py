"""
32. Calculate power of a number without using pow().
"""
num = int(input("Enter a number ="))
power = int(input("Enter a power ="))

result = 1

for i in range(1, power + 1):
    result = result * num
print(result)
