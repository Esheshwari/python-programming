#find reverse
n=int(input("Enter a number: "))
t=n #n will be the initial value but fro printing we need t
rev=0
while n!=0:
    print("Value of n is", n)
    r=n%10
    print("Value of r is", r)
    rev=rev*10+r
    print("Value of n is", n)
    n=n//10
print("Reverse of number", t, "is", rev)
