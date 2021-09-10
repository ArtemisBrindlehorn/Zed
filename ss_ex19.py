# I am a line that defines a function and says it will use two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def this_guy(dudes_name):
    print("Do you know this guy?")
    print(f"This guy named {dudes_name}?")
    print("The {} abides...\n".format("dude"))

some_guy = "Moe"
this_guy(some_guy)


# I am a line that is a precursor to calling a function
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# I am a line that references variables used as arguments
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# I am a rogue wave
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# I am rogue one talking about doing math inside a function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# I am Admiral Ackbar saying, "It's a traaaaaap!," and then eating lots of crackers
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
