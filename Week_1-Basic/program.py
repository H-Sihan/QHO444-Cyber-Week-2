num1 = int(input("Enter you 1st num: "))
num2 = int(input("Enter you 2nd num: "))
num3 = int(input("Enter you 3rd num: "))

even_num = 0
odd_num = 0

if num1 % 2 == 0:
    even_num = even_num + 1
else:
    odd_num = odd_num + 1
    
if num2 % 2 == 0:
    even_num = even_num + 1
else:
    odd_num = odd_num + 1
    
if num3 % 2 == 0:
    even_num = even_num + 1
else:
    odd_num = odd_num + 1
    
print(f"there were {even_num} even and {odd_num} odd numbers")