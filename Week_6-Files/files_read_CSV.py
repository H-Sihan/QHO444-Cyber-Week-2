import csv

with open("movies.csv") as abc:
    # Open data next assign that data to a variable
    # which is csv_file
    
    csv_reader = csv.reader(abc, delimiter=',', quotechar='"')
    # Variable 
    
    for row in csv_reader:
        print(row[1])