"""
31. Generate first n odd numbers.
"""
n = int(input("Enter N natural Number ="))
count = 0
i= 1

while i <=n :
    if i % 2 != 0:
        print(i)
        count = count + 1
    i =i+1

