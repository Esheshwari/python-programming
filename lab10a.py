#print even numbers upto n
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i % 2 == 0:  # Check if the number is even
        print(i, end=" ")

