# Built-IN Functions/Standard-Library

y = max(45, 89, 75, 89, 56, 43)
print("The maximum value is",y)

x = min(5, 90, 58, 63, 40)
print("The minimum value is",x)

# User-defined Functions
def school():
    print("eMobilis")

school()

def add():
    num1 = 5
    num2 = 3
    print(num1+num2)
add()
 #Parameter/Variable and Argument/Value
def multiply(a , b):
    print(a*b)
multiply(6,5)
multiply(10,56)
multiply( 5,20)

def employee(name,age,gender,salary,position):
    print(name,age,gender,salary,position)
employee("Maureen",25,"Female",560000,"CEO")
employee("John",52,"Male",60000,"Secretary")
employee("Mary",28,"Female",56000,"Accountant")
employee("Jesus",30,"Male",50000,"Managing Director")

# A program to display details of 5 patients in a hospital
# Using a user-defined function implement parameter and argument
# Full names,gender,age,disease

def patient(fullname,age,gender,disease):
    print(fullname,age,gender,disease)
patient("Hams Minn",45,"Male","Malaria")
patient("Teresa Don",56,"Female","Diabetes")
patient("Hannah Montana",25,"Female","Dry cough")
patient("Henry Hart",35,"Male","Pneumonia")
patient("Ashley Smith",25,"Female","Chicken Pox")