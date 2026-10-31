"""
Problem Statement: Create a simple hotel booking calculator. The room price depends on room type and
the number of nights. Customers may also receive a discount based on their stay.
"""

from colorama import Style,Fore,Back,init
init(autoreset=True)

guest_name = input("Enter a Name =").strip().title()
if guest_name == "":
    print("Please Enter a Name.")
elif not guest_name.replace(" ","").isalpha():
    print("Only Character Allowed.")
else:
    room_type = input("Room type: (Standard, Deluxe, Suite =)").lower()

    if room_type =="":
        print("Please Enter a Room Type.")
    elif not room_type.replace(" ","").isalpha():
        print("Only Character Allowed.")
    elif room_type not in ['standard','deluxe','suite']:
        print(Fore.RED + "Please, Enter Valid Occupation Risk !!")
    else:
        no_nights = input("Enter a Number of Nights =").strip()
        if no_nights =="":
            print("Please Enter a Number of Nights =")
        elif not no_nights.isdigit():
            print("Only Digits are Allowed.")

        else:

            if room_type =='standard': 
                room_price =2000   
            elif room_type =='deluxe':
                room_price = 3500
            elif room_type =='suite':
                room_price = 6000
            else:
                print("Invalid")

            no_nights =int(no_nights)
            if no_nights <= 0:
             print("Invalid number of nights.")

            if no_nights >=10:
                discount_percent =20 
            elif no_nights >= 5:
                discount_percent = 10
            else:
                discount_percent = 0
 
            room_charge = room_price *no_nights
            discount = room_charge * discount_percent /100
            final_amount =  room_charge - discount

            print("Guest Name =",guest_name)
            print("Room Type = ",room_type)
            print("Number of Nights =",no_nights)
            print("Room Charge =",room_charge)
            print("Discount Amount =",discount)
            print("Discount Percentage =",discount_percent,"%")
            print("Final Booking Amount =",final_amount)

            

