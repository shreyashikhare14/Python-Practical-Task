"""
Problem Statement: Build a mobile data billing program for a telecom customer. The monthly bill
depends on the selected plan and additional data usage.
"""

print("---------------------MOBILE DATA PLAN SYSTEM---------------------")
print("-"*80)

cust_name = input("Enter a Name = ").strip().title()
if cust_name =="":
    print("Please,Enter a Name")
elif not cust_name.replace(" ","").isalpha():
    print("Only Character Allowed.")
else:
    plan_type = input("Enter a Plan Type(Basic, Standard, Premium)").strip().lower()

    if plan_type =="":
        print("Please Enter a Plan Type !!")
    elif plan_type not in ['basic','standard','premium']:
        print("please Enter a Valid Plan Type.")
    else:

        extra_data = input("Enter a how much GB data Use in GB = ").strip().lower()

        if extra_data =="":
            print("This Field is Required !!")
        elif not extra_data.isdigit():
            print("Only Digits Are Allowed.")
        else:
        
            if plan_type =='basic':
                base_charge =299
                included_data = 10
            elif plan_type =='standard':
                base_charge = 499
                included_data = 25
            elif plan_type == 'premium':
                base_charge = 799
                included_data = 50

            extra_data = float(extra_data)
            if extra_data < 0:
                print("Invalid data usage")

            else:
                extra_data_charge = extra_data * 20

                if extra_data > 10:
                    surcharge = 100
                else:
                    surcharge = 0

                final_bill = base_charge + extra_data_charge + surcharge

                print("-"*80)
                print("Customer name is = ",cust_name)
                print("Plan Type is = ",plan_type)
                print("Base Plan Charge is = ",base_charge)
                print("Extra Data Charge is =", extra_data_charge)
                print("Surcharge is = ",surcharge)
                print("Final Bill Amount is = ",final_bill)



