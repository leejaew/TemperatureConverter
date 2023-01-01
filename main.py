while True:
    # Prompt the user to enter their temperature scale
    scale = input("Which temperature scale do you use? (Enter C for Celsius or F for Fahrenheit): ")
    
    # Convert the user input to uppercase for easier comparison
    scale = scale.upper()
    
    # If the user enters C for Celsius, ask for the temperature in Celsius
    if scale == "C":
        temperature = float(input("Enter the temperature in Celsius: "))
        # Convert the temperature from Celsius to Fahrenheit
        temperature = temperature * 9/5 + 32
        # Print the temperature in Fahrenheit
        print(f"The temperature in Fahrenheit is {temperature}.")
        break
    # If the user enters F for Fahrenheit, ask for the temperature in Fahrenheit
    elif scale == "F":
        temperature = float(input("Enter the temperature in Fahrenheit: "))
        # Convert the temperature from Fahrenheit to Celsius
        temperature = (temperature - 32) * 5/9
        # Print the temperature in Celsius
        print(f"The temperature in Celsius is {temperature}.")
        break
    # If the user enters an incorrect value, prompt them to try again
    else:
        print("Incorrect input. Please try again.")
