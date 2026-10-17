from colorama import Fore,Style, init
init(autoreset= True)
total= int(input("Enter a Total Amount ="))
if total > 2000:
    discount = total *50/100 
else:
    discount = total * 10 /100
final_discount = total - discount
print(Fore.BLUE + "Total Shopping Amount is =",total)
print(Fore.GREEN + "Discount Amount is =",discount)
print(Fore.RED + "Final Amount to Pay =",final_discount)