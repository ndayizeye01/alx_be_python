# Prompt the user to enter the first number and convert it to a float
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number and convert it to a float
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation: +, -, *, or /
operation = input("Choose the operation (+, -, *, /): ")

# Initialize the result variable to store the outcome of the calculation
result = 0

# Use match-case to determine which operation the user selected
match operation:
    case "+":  # If the user chose addition
        result = num1 + num2  # Add the two numbers
        print(f"The result is {result}.")  # Print the result
    case "-":  # If the user chose subtraction
        result = num1 - num2  # Subtract the second number from the first
        print(f"The result is {result}.")  # Print the result
    case "*":  # If the user chose multiplication
        result = num1 * num2  # Multiply the two numbers
        print(f"The result is {result}.")  # Print the result
    case "/":  # If the user chose division
        try:
            result = num1 / num2  # Attempt to divide the first number by the second
            print(f"The result is {result}.")  # Print the result
        except ZeroDivisionError:  # Handle division by zero
            print("Cannot divide by zero.")  # Print an error message if num2 is 0

