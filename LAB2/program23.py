num = int(input("Enter a three-digit number: "))
sum = 0 # Initialize sum
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
print("The sum of the cubes of the digits is:", sum)
