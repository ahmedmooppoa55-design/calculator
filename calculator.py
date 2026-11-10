class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


calc = Calculator()
operations = ["add", "subtract", "multiply", "divide"]

print("Welcome to the calculator!")
while True:
    print("Available operations: add, subtract, multiply, divide, exit")
    operation = input("Choose an operation: ")

    if operation == "exit":
        break
    if operation not in operations:
        print("Invalid operation, try again.")
        continue

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if operation == "add":
            print("Result:", calc.add(x, y))
        elif operation == "subtract":
            print("Result:", calc.subtract(x, y))
        elif operation == "multiply":
            print("Result:", calc.multiply(x, y))
        else:
            print("Result:", calc.divide(x, y))
    except ValueError as e:
        print("Error:", e)