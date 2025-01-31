import random
# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = 0
attempts = 0
print("I'm thinking of a number between 1 and 100.")
while guess != secret_number:
    guess = int(input("Take a guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
print(f"Congratulations! You guessed the number in {attempts} attempts.")
