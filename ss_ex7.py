#this line prints the classic opening to the tune
print("Mary had a little lamb.")
#this line prings the second line, using the format string function to place 'snow' in the escape characters {}
print("Its fleece was white as {}.".format('snow'))
#this is the next line, printed as we would expect
print("And everywhere that Mary went.")
#this is not a line of the rhyme, but takes the period character and prints it ten (10) times
print ("." * 10) # what'd that do?

end1 = "C"  #end1 is assigned the value C
end2 = "h"  #end2 is assigned the value h
end3 = "e"  #end3 is assigned the value e
end4 = "e"  #end4 is assigned the value e
end5 = "s"  #end5 is assigned the value s
end6 = "e"  #end6 is assigned the value e
end7 = "B"  #end7 is assigned the value B
end8 = "u"  #end8 is assigned the value u
end9 = "r"  #end9 is assigned the value r
end10 = "g" #end10 is assigned the value g
end11 = "e" #end11 is assigned the value e
end12 = "r" #end12 is assigned the value r

# watch the end = " " at the end. try removing it and see what happens
#the end=' ' acts as a separator between the two pring statements. It may be added between arguments in the print function as well
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
#classic concatenation of the strings in end7 through end12, resulting in the word Burger
print(end7 + end8 + end9 + end10 + end11 + end12)
