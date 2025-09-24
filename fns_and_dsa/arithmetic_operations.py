def perform_operation(num1, num2, operation):
    
    results = 0
    match operation:
        case "add":
            results = num1 + num2
        case "subtract":
            results = num1 - num2
        case "multiply":
            results = num1*num2
        case "divide":
            try:
                results = num1/num2
            except ZeroDivisionError:
                results = "Cannot divide by zero."
    
    return results
