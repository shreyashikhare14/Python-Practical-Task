"""
                Mini Project 1: Daily Expense Tracker
"""
print("--------------Daily Expense Tracker------------------")
while True :

    num_days= int(input("Enter a number of days = "))

    if num_days >0:
        break   
    else:
        print("Please Enter Valid number of days ")

total = 0
highest = 0

for i in range(1,num_days + 1):

    while True:

        expenses = int(input("Enter a Expenses = "))

        if expenses >= 0 :
            break
        else:
            print("Expenses cannot be negative.")

    total = total + expenses

    if expenses > highest:
        highest = expenses

avg_exp = total / num_days 

print("Total Expenses is =",total)
print("Average Expenses is = ",avg_exp)
print("highest Expenses is = ",highest)

if total > 5000:
    print("Budget Alert! You have exceeded your budget.")
else:
    print("You are within your budget.")




