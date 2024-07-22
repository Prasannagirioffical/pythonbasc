choice = input("enter your choice (+ - * /)")
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
if choice == "+":
    print(f"The sum of {a} and {b} is: ", a+b)
elif choice == "-":
     print(f"The subtraction of {a} and {b} is: ", a-b)
elif choice == "*":
     print(f"The product of {a} and {b} is: ", a*b)
elif choice == "/":
     print(f"The division of {a} and {b} is: ", a/b)
else:
    print("the input is invalid")
         