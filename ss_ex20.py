# the big two-zero!

# this guy here grabs arguments from the command line as variables to call
from sys import argv

# thie here line says, ok Bob, the first argument is the script, the second is
# the input file that we want to open
script, input_file = argv

# a function that takes the provided file object and prints all of it
def print_all(f):
    print(f.read(), end = "")

# a function that returns to the zeroth position in the provided file object
def rewind(f):
    f.seek(0)

# a function that prints a numbered line from the given file object
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

# assignment of the opened input file as a file object named current_file
current_file = open(input_file)

# we want to know what the whole file is
print("First let's print the whole file:\n")

# we print the whole file (given the file obejct argument)
print_all(current_file)

# more billboarding
print("Now let's rewind, kind of like a tape:")

# hey, we changed our position!!
rewind(current_file)

# 3 billboards outside Ebbing, Mo
print("Let's print three lines:")

# it prints the first line
current_line = 1
print_a_line(current_line, current_file)

# it prints the second line (first line plus one)
current_line = current_line + 1
print_a_line(current_line, current_file)

# it prints the third line (second line plus one)
current_line += 1
print_a_line(current_line, current_file)
