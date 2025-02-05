lst = [10, 2, 4, 1, 6]
print(lst)  # [10, 2, 4, 1, 6]
lst.sort()
print(lst)  # [1, 2, 4, 6, 10]
print(id(lst),id(lst.sort()))
