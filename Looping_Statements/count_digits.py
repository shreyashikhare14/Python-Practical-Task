digits = int(input("Enter a Digit ="))

count = 0 

while digits > 0 :
    count = count + 1
    digits = digits // 10 
print("Total Number of Digits =",count)
