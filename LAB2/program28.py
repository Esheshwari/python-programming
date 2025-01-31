def multiply(x, y): # x,y are parameter
    return x * y
print(multiply(2, 3)) # 2,3 are arguments
#No Arguments, No Return Value:
def greet():
    print("Hello!")
greet()
#No Arguments, With Return Value:
def pi():
    return 3.14
print(pi())
#With Arguments, No Return Value:
def display(message):
    print(message)
display("Hello, World!")
#With Arguments, With Return Value:
def add(a, b):
    return a + b
print(add(5, 7))
