"""
45. Print numbers skipping multiples of 3.
"""

num = int(input("Enter a Number ="))

for i in range(1,num + 1):
    if i % 3 == 0:
        continue

    print(i)