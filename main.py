#program to predict the random number made by the computer
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess an integer between 1 and {x}"))
        if guess < random_number:
            print("Guess again, Too Low")
        elif guess > random_number:
            print("Guess again, Too High")
     
    print(f"Wow! Congrats you have guessed the number \
         {random_number}")   

guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" or "C":
        if low != high:
            guess = random.randint(low,high)
        feedback = input(f"Is {guess} too high(H), too low(l), or correctly(C)?")
        if feedback == "h" or "H":
            high = guess - 1
        elif feedback == "l" or "L":
            low = guess + 1
    print(f"Wow! the computer guess your number, {guess}, correctly!")
    
computer_guess(10)