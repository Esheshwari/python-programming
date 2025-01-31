def outer_func():
    b = 20 # Local to outer_func
    print("b =", b)
    def inner_func():
        c = 10 # Local to inner_func
        print("c =", c)
        print("a in innerloop =",a)
    inner_func()
a = 1 # Global variable
print("a =", a)
outer_func()
