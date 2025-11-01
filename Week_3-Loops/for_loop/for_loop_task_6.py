user = input("What phrase do you want to see in reverse? ")

print("\nReversing...\n")
print("The phrase is ", end="")

for count in range(len(user) -1, -1, -1):
  print(user[count], end="")