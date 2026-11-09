"""
30. Generate first n even numbers.
"""
n = int(input("Enter a n natural number ="))
i=1
count = 0

while i<=n :
    if i % 2==0:
        print(i)
        count = count + 1

    i = i+1