from datetime import datetime, date,timedelta  

# Function to get the current date and time
def display_current_datetime():
    return datetime.now()   # Returns the current date and time (YYYY-MM-DD HH:MM:SS)

# Call the function and store the result in a variable
current_date = display_current_datetime()
print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")   # Print the current date and time

# Ask the user how many days they want to add to the current date
days = int(input("Enter the number of days to add to the current date: "))

# Function to calculate the future date
def calculate_future_date():
    # Returns today's date plus the number of days entered by the user
    return current_date + timedelta(days=days)

# Call the function and store the result
future_date = calculate_future_date().strftime("%Y-%m-%d")
print(f"Future date: {future_date}")   # Print the calculated future date
