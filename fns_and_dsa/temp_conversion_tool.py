# Conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9   # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5   # Factor to convert Celsius to Fahrenheit

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Get temperature input from the user
temperature = float(input("Please enter a numeric value for the temperature to convert: "))

# Ask the user which unit the input temperature is in
type_of_temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()

# Determine the conversion based on the user's input
if type_of_temperature == 'F':
    # Convert Fahrenheit to Celsius
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
elif type_of_temperature == 'C':
    # Convert Celsius to Fahrenheit
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
else:
    # Handle invalid input
    print("Invalid temperature")
