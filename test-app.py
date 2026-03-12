def add(a, b):
    return a + b

name = input("What is your name?")
print(f"Hello, {name}! Welcome back to programming after some time.")

print("--- Modern Python Calc ---")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)
print(f"The sum is: {result}")