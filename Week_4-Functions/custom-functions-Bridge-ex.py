def cross_bridge(steps):
    for i in range(1, steps):
        print(f"Crossed step {i}")
    
    if steps > 5:
        print("The bridge is collapsing...")
    else:
        print("We must keep going!")
   
user = int(input("Enter your steps: "))     
cross_bridge(user)