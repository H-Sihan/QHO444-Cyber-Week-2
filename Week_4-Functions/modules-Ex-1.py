import random

min_value  = int(input("Please enter the minimum value: "))

max_value = int(input("Please enter the Maximum value: "))

random_number = random.randrange(min_value, max_value)

print(f"""I am thinking of a number between 
      {min_value} and {max_value}. 
      Can you guess what it is?""")

print("Can you guess the number? ")

gussed_correctly = False

while not gussed_correctly:
    guess = int(input("Please enter a number: "))
    
    if guess == random_number:
        print("You guessed correctly....")
        gussed_correctly = True
    elif guess > random_number:
        print("Guess number is too high")
    else:
        print("Guess number is lower")
        
print("Game over...")