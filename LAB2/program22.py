num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
evensum = 0
oddsum = 0
if num1 > num2:
    num1, num2 = num2, num1
while num1 <= num2:
    if num1 % 2 == 0:
        evensum += num1
    else:
        oddsum += num1
    num1 += 1
print("Sum of even numbers:", evensum)
print("Sum of odd numbers:", oddsum)
