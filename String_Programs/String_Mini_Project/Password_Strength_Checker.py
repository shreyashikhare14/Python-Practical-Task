"""
Password Strength Checker
"""
from colorama import Fore , Style , init 
init(autoreset=True)

print("======================Password Strength Checker==========================")

password = input("Enter a Password = ")

if len(password) >= 8 and len(password) <=16:
    print("Password Length is valid.")
else:
    print(Fore.RED + "Password must be contain at least 8 to 16 characters. ")

upper_count = 0
lower_count = 0
digit_count =0
spe_char_count =0
for i in password:
    if i.isupper():
        upper_count = upper_count + 1
        
    if i.islower():
            lower_count = lower_count + 1

    if i.isdigit():
         digit_count = digit_count + 1

    if not i.isalnum() and not i.isspace():
         spe_char_count = spe_char_count + 1
         
        
if upper_count == 0:
    print(Fore.RED + "Password must contain at least one uppercase letter.")

if lower_count == 0:
    print(Fore.RED + "Password must contain at least one lowercase letter.")

if digit_count == 0:
     print(Fore.RED + "Password must contain at least one Digit number.")

if spe_char_count == 0:
     print(Fore.RED + "Password must contain at least one special character.")

score = 0
if upper_count > 0:
     score = score + 1

if lower_count > 0:
     score = score + 1

if digit_count > 0:
     score = score + 1

if spe_char_count > 0:
     score = score + 1

if len(password) >= 8 and len(password) <= 16:
     score = score + 1

if score <=2:
     print(Fore.RED + "Password Strength : weak ")

elif score <=4:
     print(Fore.GREEN + "Password Strength : Medium")

else:
     print(Fore.MAGENTA + "Password Strength : Strong ")

