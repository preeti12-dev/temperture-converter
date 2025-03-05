temp_value = float(input("Enter the temperature value: "))
from_unit = input("Enter the unit to convert from (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
to_unit = input("Enter the unit to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

# Perform the conversion based on the units
if from_unit == 'C' and to_unit == 'F':
    # Convert Celsius to Fahrenheit
    result = (temp_value * 9/5) + 32
    print(f"{temp_value} °C is equal to {result} °F")
elif from_unit == 'F' and to_unit == 'C':
    # Convert Fahrenheit to Celsius
    result = (temp_value - 32) * 5/9
    print(f"{temp_value} °F is equal to {result} °C")
elif from_unit == 'C' and to_unit == 'K':
    # Convert Celsius to Kelvin
    result = temp_value + 273.15
    print(f"{temp_value} °C is equal to {result} K")
elif from_unit == 'K' and to_unit == 'C':
    # Convert Kelvin to Celsius
    result = temp_value - 273.15
    print(f"{temp_value} K is equal to {result} °C")
elif from_unit == 'F' and to_unit == 'K':
    # Convert Fahrenheit to Kelvin
    result = (temp_value - 32) * 5/9 + 273.15
    print(f"{temp_value} °F is equal to {result} K")
elif from_unit == 'K' and to_unit == 'F':
    # Convert Kelvin to Fahrenheit
    result = (temp_value - 273.15) * 9/5 + 32
    print(f"{temp_value} K is equal to {result} °F")
else:
    print("Invalid unit conversion")