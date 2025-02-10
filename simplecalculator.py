#allow add,subtraction,division,multiplication
#first number,operator,second number--entered an invalid operator
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
opr = input("Enter operation: ")
if opr == "+":
    ans =(number1 + number2)
    print(ans)
elif opr == "-":
    ans =(number1 - number2)
    print(ans)
elif opr == "*":
    ans = (number1 * number2)
    print(ans)
elif opr == "/":
    ans =(number1 / number2)
    print(ans)
else:
    print("Invalid operation")
