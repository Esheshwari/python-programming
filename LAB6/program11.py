# Create a list of 10 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open('numbers.txt', 'w') as file:
    for number in numbers:
        file.write(f"{number}\n")

print("List of numbers has been written to 'numbers.txt'.")
