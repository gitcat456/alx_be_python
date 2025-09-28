# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global conversion factor
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global conversion factor
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction and conversions
    """
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # This will raise ValueError if not numeric
        
        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform conversion based on unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Error: Invalid temperature. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()