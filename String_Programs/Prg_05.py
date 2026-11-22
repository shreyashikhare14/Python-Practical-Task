"""
5. Count the number of consonants in a string.

"""
conso = input("Enter a String Name  =").lower()
count =0

for i in conso :
    # if i != 'a' and i != 'e' and i != 'i' and i !='o' and i !='u' :
    if i.isalpha() and i not in 'aeiou':
        count = count + 1
print("Total Count of Consonants is = ",count)