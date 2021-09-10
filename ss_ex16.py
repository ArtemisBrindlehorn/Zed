from sys import argv

script, filename = argv

print("We're going to erase {fileneam}.")
print("If you don't want to do that press CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#this just holds the position to allow for input by the user before moving on
input("?")

print("Opening the file...")
#opens the file in write mode, using the file object "target"
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#truncates the file, or rewrites over top starting from position 0
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("We're going to try this again in a single commande: ")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()
