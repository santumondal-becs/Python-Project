print("--- Simple Python Calculator ---")

# 1. Get the numbers from the user and convert to float (decimals)
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# 2. Display the options
print("\nChoose an operation:")
print("+ : Add")
print("- : Subtract")
print("* : Multiply")
print("/ : Divide")

# 3. Get the choice from the user
operation = input("Enter the symbol (+, -, *, /): ")

# 4. Perform the math based on the symbol chosen
if operation == "+":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif operation == "/":
    # Prevent crashing if the user tries to divide by zero
    if num2 == 0:
        print("\nError: You cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid operation symbol. Please run the program again.")