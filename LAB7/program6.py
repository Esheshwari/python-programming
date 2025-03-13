try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
finally:
    file.close()
    print("File closed.")
