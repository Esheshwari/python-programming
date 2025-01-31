import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
dis = (b ** 2) - (4 * a * c)
if dis < 0:
    print("No real roots exist.")
else:
    root1 = (-b + math.sqrt(dis)) / (2 * a)
    root2 = (-b - math.sqrt(dis)) / (2 * a)
print("Root 1:", root1)
print("Root 2:", root2)
