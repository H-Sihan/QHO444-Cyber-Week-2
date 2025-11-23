def directionWithLoop():
    movements = ["Move Forward",10, "Move Backward",5,
                 "Turn Left",3, "Turn Right",1 ]
    return movements

def run_task3():
    print("Moving...")
    path = directionWithLoop()
    
    for index in range(0, len(path), 2):
        print(f"{path[index]} for {path[index + 1]} steps")