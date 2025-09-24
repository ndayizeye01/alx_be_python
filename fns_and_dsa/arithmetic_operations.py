def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
    float/str: Result of the arithmetic operation or error message for division by zero
    """

    # Initialize the result variable
    results = 0

    # Use match-case to determine which operation to perform
    match operation:
        case "add":
            # Add the two numbers
            results = num1 + num2
        case "subtract":
            # Subtract the second number from the first
            results = num1 - num2
        case "multiply":
            # Multiply the two numbers
            results = num1 * num2
        case "divide":
            # Attempt to divide, handle division by zero
            try:
                results = num1 / num2
            except ZeroDivisionError:
                results = "Cannot divide by zero."
        case _:
            #Hndling invalid operation
            results = "Invalid Operation."

    # Return the computed result
    return results
