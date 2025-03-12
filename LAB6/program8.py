print("...Mode3(line by line)")
with open("textFile.txt", "r") as f:
    #print(f.readlines())
    for line in f:
        print(line.split(" "))
print(" ")
