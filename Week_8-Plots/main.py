import tui as ui
import process as p
import lib as visual
import plots as plt

def runMenu():
    ui.menu()

def runP():
    runMenu()
    a = p.sum(2,3)
    print(a)

def runV():
    runMenu()
    visual.run_task_1()

def plots():
    plt.run_task_2()

if __name__ == '__main__':
    plots() 

#print(a)

