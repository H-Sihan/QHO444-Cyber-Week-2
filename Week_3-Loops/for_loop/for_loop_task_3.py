user = int(input("How far we are from target? "))

print()

for target in range(user, 0, -1):
  print(f"{target} steps remaining..")
  
print("Target achieved!")