my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth usually {my_teeth} depending on the coffee.")

# this line tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")


print("================================")

name = 'Zed A. Shaw'
age = 35 # not a lie
height = round(74 * 2.54) # inches
weight = round(180 * 0.4536) # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth usually {teeth} depending on the coffee.")

# this line tricky, try to get it exactly right
total2 = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total2}")
