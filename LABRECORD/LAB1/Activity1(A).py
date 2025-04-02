import math

def calculator():
    print("Extended Calculator")
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    
    print("Select operation(s): (comma-separated)")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")
    
    choices = input("Enter choice(s) (1,2,3...): ").split(',')
    
    for choice in choices:
        choice = choice.strip()
        if choice == '1':
            print(f"Addition: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Division: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is undefined.")
        elif choice == '5':
            print(f"Modulus: {num1} % {num2} = {num1 % num2}")
        elif choice == '6':
            print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")
        elif choice == '7':
            print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
        else:
            print(f"Invalid choice: {choice}")

calculator()
