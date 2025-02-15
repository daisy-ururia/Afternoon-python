# Python program to display
# a multiplication table

def multiplication_table(number,upto=10):
    for i in range(1,upto+1):
        print(number,"x",i,"=",number*i)

num = int(input("Enter number: "))
multiplication_table(num)