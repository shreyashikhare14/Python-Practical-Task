"""
Develop an insurance premium calculator. The premium category depends on age,
occupation risk, and smoking status.
"""
from colorama import Fore , Style ,Back,init
init(autoreset= True)
customer_name = input("Enter a Name =").strip().title()

if customer_name =="":
        print(Fore.RED+"Please Enter a Name.")
elif not customer_name.replace(" ","").isalpha():
         print(Fore.RED+"Only Alphabets Allowed.")
else:
    age  = input("Enter a Age =")
    if age == "":
     print(Fore.RED+"Please,Enter a Age.")
    elif not age.isdigit():
     print(Fore.RED+"Only Digit Allowed.")

    else:
        age=int(age)
        if age <=18:
            print(Fore.RED+"You are not eligible")
            
        else:
            base_premium = 10000
            additional_charge =0
            if age > 50:
                additional_charge += 5000

            occupation_risk=input("Enter Occupation risk(Low, Medium, High) =").lower().strip()
            if occupation_risk == "":
                print(Fore.RED+"This Field Required !!")

            elif not occupation_risk.replace(" ","").isalpha():
                print(Fore.RED+"Only Charcters Allows")

            elif occupation_risk not in ['low','medium','high']:
                print(Fore.RED+"Please, Enter Valid Occupation Risk !!")

            else:    

             if occupation_risk == 'high':
                additional_charge = additional_charge + 7000

             elif occupation_risk== 'medium':
                additional_charge = additional_charge + 3000

             elif occupation_risk == 'low':
                additional_charge = additional_charge + 0
                 
             smoker = input("Are You Somker (yes /no )= " ).lower().strip()
             if smoker == "":
                print(Fore.RED+"Please , Enter the Somking Status !! ")

             elif not smoker.replace(" ","").isalpha():
                            print(Fore.RED+"Only Charcters Allows")
             elif smoker not in ['yes', 'no']:
                print(Fore.RED+"Please, Enter a Valid Answer.") 

             else:
            
              if smoker == 'yes':
                 additional_charge = additional_charge +5000
            
              final_premium = base_premium + additional_charge

              print("-"*80)
              print(Fore.BLACK + "Name of Customer is = ",customer_name)
              print(Fore.GREEN+"Your Age is = ",age)
              print(Fore.BLUE+"Your Base Primium is =",base_premium)
              print(Fore.LIGHTBLACK_EX+"Additional Charges is =",additional_charge)
              print(Fore.CYAN+"Final Premium is =",final_premium)
        
              if additional_charge >=10000:
                print(Fore.RED+"High Risk Policy")

       

