print("...Mode2(line by line)")
with open("textFile.txt", "r") as f:
    print("Line1: ", f.readline(), end="")
    print("Line2: ", f.readline(), end="")
print(" ")
