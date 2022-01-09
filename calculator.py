# Python Program to Make a Simple Calculator

def multiplication(num0, num1):
    return num0 * num1


def addition(num0, num1):
    return num0 + num1


def subtraction(num0, num1):
    return num0 - num1


def divide(num0, num1):
    return num0 / num1


value1 = int(input("Enter 1st number: "))
value2 = int(input("Enter 2nd number: "))

print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction")

operation = int(input("Choose operation 1/2/3/4: "))
if operation == 1:
    print(value1, "/", value2, "=", divide(value1, value2))

if operation == 2:
    print(value1, "*", value2, "=", multiplication(value1, value2))
if operation == 3:
    print(value1, "+", value2, "=", addition(value1, value2))
if operation == 4:
    print(value1, "-", value2, "=", subtraction(value1, value2))
else:
    print("Enter correct operation")
