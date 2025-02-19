#print upper pyramid of numbers
rows=int(input("Enter a num: "))
for i in range(1, rows+1):
    print(" "*(rows-i)+" ".join(str(num) for num in range(1, i+1)))
