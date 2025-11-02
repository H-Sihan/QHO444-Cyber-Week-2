user = int(input('Please enter a sequence: '))

marker = input("Please enter the character for the marker: ")

maker1 = -1
maker2 = -1

for position in range(0, len(user), 1):
    letter = user[position]
    
    if letter == marker:
        if (maker1 == -1):
            maker1 = position
        else:
            maker2 = position
            
print(f"The distance between the markers is {maker2 - maker1 -1}.")