user = int(input("How mant obstacles must avoid? "))

obstacles_avoided = 0

print()

# 
while obstacles_avoided < user:
    print("Avoiding...", end="")
    obstacles_avoided = obstacles_avoided + 1
    print(f"Done! {obstacles_avoided} obstacles avoided")