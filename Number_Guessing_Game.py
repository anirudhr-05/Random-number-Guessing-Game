import random

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

guessed_number = int(input("\nEnter your guess: "))

while guessed_number != secret_number:
    if guessed_number < 1 or guessed_number > 100:
        print("The Guessed number is out of range! Please guess a number between 1 and 100.")
    elif guessed_number < secret_number:
        print("The guess is Low!")
    else:
        print("The guess is High!")
        
    attempts += 1
    print("Attempts taken:", attempts)
    guessed_number = int(input("\nEnter your next guess: "))

attempts += 1 
print("Congratulations! The number is Correct and you Guessed it in :", attempts,"Attempts")
