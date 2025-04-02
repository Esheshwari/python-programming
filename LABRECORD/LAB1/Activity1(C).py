def find_largest():
    print("Find the largest of five numbers:")
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    num3 = float(input("Enter 3rd number: "))
    num4 = float(input("Enter 4th number: "))
    num5 = float(input("Enter 5th number: "))

    largest = max(num1, num2, num3, num4, num5)

    print(f"Largest number: {largest}")

find_largest()
