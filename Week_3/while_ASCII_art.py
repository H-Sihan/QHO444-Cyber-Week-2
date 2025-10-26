user = int(input("How many bars should be charged? "))

bars_charged = 0

print()

while bars_charged < user:
    bars_charged = bars_charged + 1
    print(f"Charging: {'█' * bars_charged}")
    
print("The battery is fully charged.")