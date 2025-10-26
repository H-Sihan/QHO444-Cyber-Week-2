# The program should start by 
# asking the user to enter the 
# cover type (hard or soft) of the book.
# If the book has a "soft" cover then 
# the program should ask the user 
# if the book is "perfect bound".
# If the answer is "yes" then the message 
# "Soft cover, perfect bound books are very popular!" 
# should be displayed
user_input = input("What type of cover does this book? ")

if user_input == "soft":
    print("Is the book perfect bond? ")
    perfect_bond = input()
    
    if perfect_bond == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft cover with coils")
else:
    print("books with hard covers can be more expensive")