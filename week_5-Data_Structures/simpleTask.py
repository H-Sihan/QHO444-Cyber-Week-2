def collectUserData():
    user = input("Please enter your name: ")
    return user

def run():
    print(collectUserData())
    
if __name__ == '__main__':
    run()