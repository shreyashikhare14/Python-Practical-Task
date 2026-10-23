"""
Problem Statement: Create a movie ticket pricing program for a cinema. 
Ticket price depends on age, show type, and whether the booking is on a weekend. 
Required Inputs 
• Customer name 
• Age 
• Show type: Morning or Evening 
• Day type: Weekday or Weekend 

Business Rules / Conditions 
Base ticket price is ₹200 
Children below 12 receive 50% discount 
Senior citizens aged 60 or above receive 30% discount  
Morning shows receive an additional ₹30 discount 
Weekend shows have a ₹50 surcharge 
Age cannot be negative Expected 

Output 
• Customer name 
• Original ticket price 
• Discount 
• Weekend surcharge 
• Final ticket price 
"""


name = input("Enter a Name = ")
age = int(input("Enter an Age = "))
show_type = input("Enter Show Type (Morning or Evening) = ").lower()
day_type = input("Enter Day Type (Weekday or Weekend) = ").lower()

original_ticket_price = 200
morning_discount = 0
weekend_charge_add = 0

if age < 0:
    print("Age cannot be Negative.")

else:
    if age < 12:
        age_discount = original_ticket_price * 50 / 100
    elif age >= 60:
        age_discount = original_ticket_price * 30 / 100
    else:
        age_discount = 0

    if show_type == "morning":
        morning_discount = 30

    if day_type == "weekend":
        weekend_charge_add = 50

    total_discount = age_discount + morning_discount
    final_ticket_price = (
        original_ticket_price - total_discount + weekend_charge_add
    )

    print("Name of the Customer =", name)
    print("Original Ticket Price =", original_ticket_price)
    print("Age Discount =", age_discount)
    print("Morning Discount =", morning_discount)
    print("Total Discount =", total_discount)
    print("Weekend Surcharge Added =", weekend_charge_add)
    print("Final Ticket Price =", final_ticket_price)
