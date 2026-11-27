"""
24. Create a list and find the average of elements.
"""

lst1 = input("Enter a Element = ")
lst = list(map(int,lst1.split()))

length = len(lst)
sum=0

for i in lst :
    sum = sum + i
avg = sum /length
print("Average of Elements is = ",avg)