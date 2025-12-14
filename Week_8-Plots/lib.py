import matplotlib.pyplot as abc

def basicPlot():
    x = [20,30,40]
    y = [0,10,40]
        
    abc.plot(x,y)
    abc.show()
    
def helloWorld():
    print("Hello from Lib.py")

def display_line(x,y):
    abc.plot(x,y)
    abc.show()
    
def run_task_1():
    print("Your plot is loading....")
    x_values = [1,2,3,4,5]
    y_values = [1,4,6,8,10]
    display_line(x_values,y_values)