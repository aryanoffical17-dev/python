f = open(r"C:\python\File_IO\demo.txt", "r") 


data = f.read()
print(data)

line = f.readline()
print(line)

line = f.readline()
print(line)

f.close()
