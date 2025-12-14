class Robot:
    
    # Class attribute
    laws = "Protect, Obey and Survive"
    
    # static method
    @staticmethod
    def the_law():
        print(Robot.laws)
        
    # class method
    @classmethod
    def assemble(cls):
        return cls("Assembled Robot")
    
    # Instance
    def __init__(self, name = "Robot"):
        
        # an instance attribute
        self.name = name
        self.age = 0
    
    # Instance method
    def display(self):
        print(f"The {self.name}")
        
        
def run():
    rob = Robot()
    print(rob.display())
    print(rob.assemble())
    print(rob.the_law())

if __name__ == '__main__':
    run()