import math

def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter temperature: "))

    print("Select the conversion(s): (comma-separated)")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choices = input("Enter choice(s) (1,2,3...): ").split(',')

    for choice in choices:
        choice = choice.strip()
        if choice == '1':
            fahrenheit = (temp * 9/5) + 32
            print(f"{temp}°C is {fahrenheit}°F")
        elif choice == '2':
            celsius = (temp - 32) * 5/9
            print(f"{temp}°F is {celsius}°C")
        elif choice == '3':
            kelvin = temp + 273.15
            print(f"{temp}°C is {kelvin}K")
        elif choice == '4':
            celsius = temp - 273.15
            print(f"{temp}K is {celsius}°C")
        elif choice == '5':
            kelvin = (temp - 32) * 5/9 + 273.15
            print(f"{temp}°F is {kelvin}K")
        elif choice == '6':
            fahrenheit = (temp - 273.15) * 9/5 + 32
            print(f"{temp}K is {fahrenheit}°F")
        else:
            print(f"Invalid choice: {choice}")

temperature_converter()
