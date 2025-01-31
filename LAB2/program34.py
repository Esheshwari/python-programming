def add(p, q):
    return p + q
def subtract(p, q):
    return p - q
def multiply(p, q):
    return p * q
def divide(p, q):
    return p / q

# Input from user
print("Select operation:")
print("a. Add")
print("s. Subtract")
print("m. Multiply")
print("d. Divide")
choice = input("Enter choice (a/s/m/d): ")
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

# Function call based on choice
if choice == 'a':
    print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
elif choice == 's':
    print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")
elif choice == 'm':
    print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")
elif choice == 'd':
    print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")
else:
    prit("Invalid input")   
