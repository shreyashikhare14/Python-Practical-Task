# Mini Project 4: Shopping Cart Total

print("--------------------Mini Project 4: Shopping Cart Total--------------------")

while True:
    num_product = int(input("Enter number of  Products :"))

    if num_product > 0 :
        break
    else:
        print("Please enter a valid number of products")

total = 0
discount =0
delivery =0

for i in range(1,num_product + 1):

        print("Product ",i)

        while True:
            price = int(input("Enter a Product Price = "))

            if price >= 0:
                break
            else:
                print("Negative Price is Not Allowed!")


        while True :
            quantity = int(input("Enter a Product Quantity ="))
        
            if quantity >= 0:
                break
            else:
                print("Negative Quantity Not Allowed !")

        item_total = price * quantity

        total =total + item_total

if total >= 3000:
    discount = total * 10 /100

else:
    discount = 0 

discounted_amount = total - discount

if discounted_amount < 1500:
    delivery = 100 
else:
    delivery = 0

final_amount = discounted_amount + delivery 


print("Subtotal = ",total)
print("Discount = ",discount)
print("Delivery Charge = ",delivery)
print("Final Payable Amount = ",final_amount)










