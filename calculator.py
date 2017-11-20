# Basic calculator that do the basic calculations like addition, subtraction, multification etc
# declaring the global variables
print("This is the basic calculator")
print("\n********************************************\n")
print("$$$$$$^^^^^^********^^^^^^^$$$$$$$$$$")
number1 = float(input('Please Enter the first number \n'))
operator = str(input("Please select the operator \n"))
number2 = float(input("Please enter the second number \n"))
def add():
    print(number1 + number2)
def sub():
    print(number1 - number2)
def mult():
    print(number1 * number2)
def devide():
    print(number1 / number2)
if(operator == "+"):
    add()
elif(operator == "-"):
    sub()
elif(operator == "*"):
    mult()
elif(operator == "/"):
    devide()
else:
    print("Wrong operator !. Please select the currect operator..")