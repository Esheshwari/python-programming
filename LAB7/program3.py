with open("output.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 35])
