from sys import argv

script, filename = argv

file = open(filename)
print("This is your file: ")
print(f"{file}")
print(file.read())
