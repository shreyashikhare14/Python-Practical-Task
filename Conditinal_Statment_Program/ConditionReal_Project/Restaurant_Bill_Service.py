"""
Problem Statement: Create a restaurant billing program for a customer. The service charge and discount
depend on the bill amount and membership status.
Required Inputs
• Customer name
• Food bill amount
• Membership: Yes or No
Business Rules / Conditions
55. Bill below ₹1,000: no discount
56. Bill from ₹1,000 to ₹2,999: 5% discount
57. Bill from ₹3,000 to ₹4,999: 10% discount
58. Bill ₹5,000 or above: 15% discount
59. Members receive an additional 5% discount
60. Add 5% service charge after discount
61. If final bill is ₹5,000 or more, display 'Thank you for being a valued customer'
Expected Output
• Customer name
• Original bill
• Discount
• Service charge
• Final payable amount
• Message
Coding Restriction: Calculate the final amount in the correct order using conditions. Do not use loops.
"""

from colorama import Fore,Style, init
init(autoreset= True)

name = input("Enter a Name =").lower().capitalize()
bill_amount = int(input("Enter a Bill Amount ="))
membership = input("If you purchase any Membership ?(Yes/No) =").lower()

#No discount Apply
if bill_amount < 1000 and bill_amount > 0 :
    discount = bill_amount * 0/100

# if amount is greater than 1000 and less than 2999 then discount will 5%
elif bill_amount >=1000 and bill_amount <=2999:
    discount = bill_amount * 5/100

# if amount is greater than 3000 and bill amount is less than 4999 than add 10%.
elif bill_amount >=3000 and bill_amount <=4999:
    discount = bill_amount * 10/100

# if amount is greater than 5000 and bill amount is less than 5000 than add 15%.
elif bill_amount >=5000 :
    discount = bill_amount * 15 /100

else:
    print("Invalid.")

# if user can purchased Membership than add 5% discount 
if membership == 'yes':
    membership_dis = bill_amount * 5/100
else:
    membership_dis = bill_amount * 0 /100

# Final total discount 
total_discount = discount + membership_dis

# Find Discount Value 
after_discount_value = bill_amount - total_discount

# Add Service Charge on after discount caculate.
service_charge = after_discount_value * 5 /100

# Find Final Amount 
final_amount = after_discount_value + service_charge

# Show All Output To User 

# 1.Name of Customer 
print(Fore.BLACK + f"Name Of The Customer = {name}")

# 2.  Original bill
print(Fore.BLUE + f"Your Original Bill is = {bill_amount}")

# 3. Discount
print(Fore.GREEN + f"Your Total Discount is ={total_discount}")

# 4.Service charge
print(Fore.LIGHTMAGENTA_EX + f"Service Charges is ={service_charge}")

# 5.Final payable amount
print(Fore.RED + f"Your Final Payable Amount is = {final_amount}")

if final_amount >= 5000:
    print(Fore.MAGENTA + "Thank you for being a valued customer")

