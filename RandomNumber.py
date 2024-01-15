import random

# Generate a random number between 1 and 20
n = random.randint(1, 20)

guess = 0
max_hints = 3  # Change this value to control the number of hints

while guess != n:
    guess = int(input("Enter your guess:"))

    if guess == n:
        print("Congratulations! You guessed it right!")
    elif guess < n:
        print("Too low!")
        hints_given = 0

        if n % 2 == 0:
            print("Hint: The number is divisible by 2.")
            hints_given += 1

        if n % 3 == 0 and hints_given < max_hints:
            print("Hint: The number is divisible by 3.")
            hints_given += 1

        if n % 5 == 0 and hints_given < max_hints:
            print("Hint: The number is divisible by 5.")
    elif guess > n:
        print("Too high!")
        hints_given = 0

        if guess - n > 5:
            print("Hint: You are quite far from the number.")
            hints_given += 1

        if n % 4 == 0 and hints_given < max_hints:
            print("Hint: The number is divisible by 4.")
            hints_given += 1

        if n % 6 == 0 and hints_given < max_hints:
            print("Hint: The number is divisible by 6.")
