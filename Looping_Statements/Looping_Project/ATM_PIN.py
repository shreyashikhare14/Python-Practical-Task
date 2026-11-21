"""
            Mini Project 3: ATM PIN Verification
"""
correct_pin = 1234
attempts = 0
access_granted = False

print("---------ATM PIN Verification System---------")

while attempts < 3:
    pin = int(input("Enter a PIN ="))

    attempts = attempts + 1

    if 1000 <= pin <= 9999:
        print("Valid PIN format")

        if pin == correct_pin :
                print("Access Granted.")
                access_granted = True
                break

        else:
             print("Incorrect PIN")

    else:
        print("PIN must be 4 digits.")

if access_granted == False:
     print("Card Temporarily Locked")

print("Attempts Used = ",attempts)

    