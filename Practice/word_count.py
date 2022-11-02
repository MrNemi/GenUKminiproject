# Read the file
file = open("names.txt")
lines = file.readlines()
print(lines)

# remove \n

# Do the hard stuff (count totals)
# Dictionary ?????
# Loop over each name (and hopefully add it to a dictionary)
name_count = {}

for name in lines:
    name = name.rstrip()
    # if name already in dictionary, add one to existing value
    if name in name_count:
        # Add 1
        current_value = name_count[name]
        print("The current value for", name, "is", current_value)
        new_value = current_value + 1
        print("The new value for", name, "is", new_value)
        name_count[name] = new_value
    # else, set value 1
    else:
        name_count[name] = 1
        
    print(name)
    
print(name_count)

# Write the results to a new file
# Name: John, Count: 4
# Name: James, Count: 1
# ...
 




# STRETCH GOAL: Add try/except