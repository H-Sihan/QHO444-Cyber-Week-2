file = open("sample.txt",'r')
content = file.readline()
print(content.strip())
file.close()