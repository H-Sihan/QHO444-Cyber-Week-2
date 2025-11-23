def direction():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right" ]
    return direction

def directionWithoutLoop():
    movements = ["Move Forward",10, "Move Backward",5,
                 "Turn Left",3, "Turn Right",1 ]
    return movements

def run_task2():
    print("Moving...")
    path = directionWithoutLoop()
    
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")
    
def directionWithLoop():
    movements = ["Move Forward",10, "Move Backward",5,
                 "Turn Left",3, "Turn Right",1 ]
    return movements

def run_task3():
    print("Moving...")
    path = directionWithLoop()
    
    for index in range(0, len(path), 2):
        print(f"{path[index]} for {path[index + 1]} steps")
    
    
def run_task1():
    print(direction())
    
if __name__ == '__main__':
    run_task3()