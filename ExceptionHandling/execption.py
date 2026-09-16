# a = input("Enter the number :")
# print(f"Multipcation table of {a} is :") 

# try:
#     for i in range(1 , 11):
#          print(f"{int(a)} x {i} = {int(a)*i}")
# except:
#      print("Some error accourd")


try:
    num = int(input("Enter an integer :"))
    a = [6 , 3]
    print(a[num])
except ValueError:
    print("Number entered is not integer .")

except IndexError:
    print("Index error")