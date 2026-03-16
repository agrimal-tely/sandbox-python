def add(a, b):
    return a + b

name = input("What is your name?")
print(f"Hello, {name}!")

print("--- Python Calc ---")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Do you want to sum (+) or subtract (-)?")
operation = input("Enter + or -: ")

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = num1 - num2
else:
    print("Invalid operation. Please enter + or -.")

print(f"The result is: {result}")
