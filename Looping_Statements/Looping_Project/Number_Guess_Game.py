#Mini Project 5: Number Guessing Game

from colorama import Style ,Fore,init
init(autoreset= True)

print(Fore.CYAN + "--------------------Mini Project 5: Number Guessing Game--------------------")

secret_number = 14
attempts= 0
max_attempts = 5
won = False

while attempts < max_attempts:
    while True :
        guess = input("Guess The Secret Number (1-100) = ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please Enter Only Numbers !!")
            continue

        if guess >=1 and guess <=100:
            break
        else:
            print("Invalid Input ! Enter a number between 1 to 100.")
    attempts = attempts + 1

    if guess == secret_number:
        print(Fore.GREEN + "Congratualation ! You Guessed the Correct Number .")
        won= True
        break
    elif guess < secret_number :
        print(Fore.YELLOW + "Too Low !")
    else :
        print(Fore.RED + "Too High !")

if won == False :
    print("You Lost ! Better Luck Next Time.")
    print(Fore.MAGENTA + "Secret Number was = ",secret_number)

print("Attempts Used = ",attempts)
