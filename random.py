import random

secret_number = random.randint(1, 100)

while True:

    user_guess = int(input("Guess the number (between 1 and 100): "))

   
    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")