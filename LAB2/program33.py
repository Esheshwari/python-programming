def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

num  = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
