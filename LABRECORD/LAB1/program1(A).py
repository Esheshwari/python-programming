def calculator():
    print("Simple Calculator")
    num1=float(input("Enter 1st num: "))
    num2=float(input("Enter 2nd num: "))
    print("Select operation:")
    print("1. add")
    print("2. divide")
    choice=input("Enter choice(1\2): ")
    if choice=='1':
        print(f"Result: {num1}+{num2}={num1+num2}")
    elif choice=='2':
        if num2!=0:
            print(f"Result: {num1}/{num2}={num1/num2}")
        else:
            print("error")
    else: print("Invalid")
calculator()
