"""
40. Count uppercase and lowercase letters separately.
"""

string = input("Enter a String = ")

upp_count =0
low_count = 0

for i in string:
    if i.islower():
        low_count = low_count + 1
    elif i.isupper():
        upp_count = upp_count + 1 
    else:
        print("Invalid")

print("Upper Count is = ",upp_count)
print("Lower Count is = ",low_count)