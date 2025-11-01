user = int(input("What level of brightness is required? "))

print("\nAdjusting brightness....\n")

for brightness in range(2, user + 1, 3):
  print(f"brightness level: {'*' * brightness}")
  
print("Complete!")