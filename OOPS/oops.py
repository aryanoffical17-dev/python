class Student:
    College_name = "IIT Delhi"
    def __init__(self ,fullname):  #function
        self.name = fullname
        # print("Adding new student in data base :")
    @staticmethod
    def Hi():
        print("hi")


    def hello(self):
        print("Welcome")

    def get_marks(self):
        return self.marks
    

s1 =Student("Aryan")
s1.hello()
print(s1.name)
print(s1.College_name)
print()
s2 =Student("Mohit")
print(s2.name)
s1.hello()
print(s2.College_name)
s1.Hi()