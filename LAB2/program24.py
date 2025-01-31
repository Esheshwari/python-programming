fact = 1
n = int(input("Enter a number: "))
if n == 0 or n == 1:
    print("Factorial is", fact)
else:
    for i in range(1, n + 1):
        fact *= i
print("Factorial is", fact)
