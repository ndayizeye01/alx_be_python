# Ask the user to input the current weather and store it in a variable
# Example inputs: "sunny", "rainy", "cold"
weather = input("What's the weather like today? (sunny/rainy/cold): ")
# Convert the input to lowercase so it works regardless of what the user types
weather = weather.lower()

# Convert the user's input to lowercase and check if it matches "sunny"
if weather == 'sunny':
    # If the weather is sunny, suggest wearing light clothing and sunglasses
    print("Wear a t-shirt and sunglasses.")

# Check if the weather is "rainy"
elif weather == 'rainy':
    # If it's rainy, suggest taking an umbrella and wearing a raincoat
    print("Don't forget your umbrella and a raincoat.")

# Check if the weather is "cold"
elif weather == 'cold':
    # If it's cold, suggest wearing warm clothing like a coat and scarf
    print("Make sure to wear a warm coat and a scarf.")

# If the input doesn't match any of the expected options
else:
    # Provide a default message for unknown weather types
    print("Sorry, I don't have recommendations for this weather.")
