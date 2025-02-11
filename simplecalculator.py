#allow add,subtraction,division,multiplication
#first number,operator,second number--entered an invalid operator
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
opr = input("Enter operation: ")
if opr == "+":
    print(number1 + number2)
elif opr == "-":
    print(number1 - number2)
elif opr == "*":
    print(number1 * number2)
elif opr == "/":
    print(number1 / number2)
else:
    print("Invalid operation")
