print("Calculating the sum of 1st 100 numbers...")

# declare
number = 1

user1 = int(input("Enter the 1st number: "))
user2 = int(input("Enter the 2nd number: (This should be more than the 1st)"))

# calculate sum of the first 100 numbers
total = 0

while user1 <= user2:
    total = total + user1
    user1 = user1 + 1
    
print(f"Done calculation... {total}")