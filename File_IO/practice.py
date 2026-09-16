with open(r"C:\python\File_IO\practice.txt" , "r") as f:
            data =f.read()

new_data = data.replace("Java" , "Python")
print(new_data)


with open(r"C:\python\File_IO\practice.txt" , "w") as f:
            f.write(new_data)
    
