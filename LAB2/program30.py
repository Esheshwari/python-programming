def print_parameters(a, b, c):
    print("1st param:", a)
    print("2nd param:", b)
    print("3rd param:", c)
# Invalid:
print_parameters(c="third", "first", "second")
