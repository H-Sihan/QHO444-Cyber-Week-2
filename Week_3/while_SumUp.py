user = int(input("How many numbers should I sum up? "))

sum = 0

print()

total = 0

while sum < user:
    print(f"Please enter the number {sum} of {user}: ")
    number = int(input())
    
    total = total + number
    sum = sum + 1
    
print(f"Display answer {total}")