# input some character
# input 0 
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:     
    print("Error: Invalid input!")
except ZeroDivisionError:
    print("Error: Division by zero!")
