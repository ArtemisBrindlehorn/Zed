#imports the argment variable function/module from the sys module collection
from sys import argv

#notes that there are two argument variables, one for the script, one for the filename
script, filename = argv

#this opens the file, filename, and writes the contents to a variable txt
txt = open(filename)

#prints a line that tells you what file is being opened
print(f"Here's your file {filename}:")
#prints whatever was in the file opened and saved as txt
print(txt.read())

#prints a line asking you to type the filename again
print("Type the filename again:")
#takes the string from the input module and assigns it to a variable file_again
file_again = input("> ")

#opens the filename in the local file given by file_again, opens it as txt_again
txt_again = open(file_again)

#prints the file txt_again using what was taken from the read module
print(txt_again.read())
