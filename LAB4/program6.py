rows=int(input("Enter a num: "))
for i in range(1, rows+1):
    print(" "*(rows-i)+" ".join(chr(65+j) for j in range(i)))
for i in range(rows-1, 0, -1):
    print(" "*(rows-i)+" ".join(chr(65+j) for j in range(i)))
