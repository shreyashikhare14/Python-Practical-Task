"""
25. Count consonants in a string.
"""

str = input("Enter a String =")
count = 0

for i in str:
    if i not in 'aeiouAEIOU':
        count = count + 1
print("Consonent Count is = ",count)