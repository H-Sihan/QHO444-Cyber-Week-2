direction = input("Towards which direction? ")

if direction == 'up':
    print("I'm moving upwards")
elif direction == 'down':
    print("I'm moving downwards")
elif direction == 'left':
    print("I'm moving left side")
elif direction == 'right':
    print("I'm moving right side")
elif direction == "None":
    print("You're blocked")
else:
    print("I'm lost")