p = "This is a Global variable"  # Global variable

def is_local(a):
    a = "This is a Local Variable"  # Local variable inside the function
    print(a)

print(p)  # This will print the global variable
is_local(p)  # Call the function with 'p' as an argument
