name = 'Zed A. Shaw'
conv_to_cent = 2.54 # number of centimeters per inch
conv_to_kilo = 0.4536 # number of kilograms per pound
age = 35 # not a lie
height = 74 * conv_to_cent# inches
weight = 180 * conv_to_kilo# pounds
eyes = 'Blue'
hair = 'Brown'
teeth = 'White'


print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky try to get it exactly correct
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
