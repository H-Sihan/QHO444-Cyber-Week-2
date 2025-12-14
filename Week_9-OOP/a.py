# robot.py
# This file defines the Robot class

class Robot:
    # Class attribute (constant)
    MAX_ENERGY = 100

    def __init__(self, ):
        """
        Initializer for the Robot class.
        Sets default values for name, age, and energy.
        """
        self.name = "Robot"
        self.age = 0
        self.energy = 0

    def display(self):
        """
        Displays the name of the robot.
        """
        print(f"I am {self.name}")


# Test code
if __name__ == "__main__":
    robot = Robot()
    robot.display()
