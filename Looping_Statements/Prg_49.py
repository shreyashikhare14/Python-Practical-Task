"""
49. Display menu-driven program using while loop.
"""
while True:
    print("\n--------MENU--------")
    print("1.ADDITION")
    print("2.SUBSTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.EXIT")

    choice= int(input("Enter a choice ="))

    if choice == 1:
        a= int(input("Enter First Number ="))
        b= int(input("Enter Second Number ="))
        print("Addition is =",a + b)

    elif choice == 2 :
        a = int(input("Enter First Number = "))
        b = int(int(input("Enter Second = ")))
        print("Substraction is = ", a - b)

    elif choice == 3 :
        a = int(input("Enter First Number = "))
        b = int(input("Enter Second Number = "))
        print("Multiplication is =", a*b)

    elif choice == 4:
        a = int(input("Enter First Number = "))
        b = int(input("Enter Second Number = "))
        print("Division is =", a/b)

    elif choice == 5:
        print("Thank For Visiting...")
        break

    else:
        print("Invalid Choice.")