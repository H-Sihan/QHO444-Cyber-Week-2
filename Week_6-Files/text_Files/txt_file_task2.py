def display_char(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(data)
        
def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)

def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)
        
def search(file_path):
    print("Searching....")
    with open(file_path) as file:
        for location in file:
            print(f'Looked in {location.strip()}')
        print("Done...!")
        
def run_task2():
    display_char("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")
    search("library.txt")

if __name__ == "__main__":
    run_task2()