def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return " it Division by zero."
    return x / y

def calculator():
    print("Select operation:")
   

    choice = input("Enter choice(+ - * /): ")

    if choice in ['+', '-', '*', '/']:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == '+':
            print(f"The addition of {a} and {b} is {add(a, b)}")

        elif choice == '-':
            print(f"The subtraction of {a} and {b} is {subtract(a, b)}")

        elif choice == '*':
            print(f"The multipliy of {a} and {b} is {multiply(a, b)}")

        elif choice == '/':
            print(f"The division of {a} and {b} is {divide(a, b)}")
    else:
        print(" the Invalid input")

calculator()