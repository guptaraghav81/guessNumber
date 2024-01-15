import random

# Generate a random number between 1 and 20
n = random.randint(1, 20)

guess = 0
while guess != n:
    guess = int(input("Enter your guess:"))

    if guess == n:
        print("Congratulations! You guessed it right!")
    elif guess < n:
        print("Too low!")


        if n % 2 == 0:
            print("Hint: The number is divisible by 2.")


        if n % 3 == 0 :
            print("Hint: The number is divisible by 3.")


        if n % 5 == 0 :
            print("Hint: The number is divisible by 5.")
    elif guess > n:
        print("Too high!")


        if guess - n > 5:
            print("Hint: You are quite far from the number.")


        if n % 4 == 0 :
            print("Hint: The number is divisible by 4.")


        if n % 6 == 0 :
            print("Hint: The number is divisible by 6.")
