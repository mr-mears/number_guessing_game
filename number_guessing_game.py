import random

random_number = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))
attempts = 1

while guess != random_number:
    attempts += 1
    if guess > random_number:
        guess = int(input("lower: "))
    elif guess < random_number:
        guess = int(input("higher: "))

print("Well done!")
print("You guessed the random number in",  attempts, "attempts.")