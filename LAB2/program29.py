#Positional Arguments: Passed in order of parameters.
def print_numbers(a, b, c):
    print(a, b, c)
print_numbers(1, 2, 3)
#Keyword Arguments: Passed using parameter names.
def print_numbers(a, b, c):
    print(a, b, c)
print_numbers(a=1, c=3, b=2)
def print_parameters(a, b, c):
    print("1st param:", a)
    print("2nd param:", b)
    print("3rd param:", c)
print_parameters(a=1, c=3, b=2)
