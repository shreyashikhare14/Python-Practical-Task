"""
16. Create a list of numbers and find max and min values.
"""
lst1 = input("Enter a List = ")
lst = list(map(int,lst1.split()))

print("Original List = ",list)

max_value = max(lst)
min_value = min(lst)

print("Maximum Marks is = ",max_value)
print("Minimum Marks is = ",min_value)
