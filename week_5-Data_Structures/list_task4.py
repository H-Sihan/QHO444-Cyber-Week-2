def direction():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right" ]
    return direction 


def menu():
    print("Please select a direction")
    direct = direction()
    for index in range(len(direct)):
        print(f"{index}: {direct[index]}")
        
    user = int(input("Enter the value: "))
    
    return direct[user]
        
def run():
    route = []
    print("Working out escape route...!")
    for count in range(3):
        route.append(menu())
    print(f"Escape route: {route}")
    
if __name__ == '__main__':
    run()
        