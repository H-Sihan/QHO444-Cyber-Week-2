# Blueprint
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 29
        self.weight = 80
        
    def abc(self):
        print("Message from func ABC")
        
def run():
    p = Person("Sihan")
    print(p.name)

if __name__ == '__main__':
    run()