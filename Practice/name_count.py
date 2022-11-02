file = open("Practice\persistence.txt", "r")
lines = file.readlines()

for line in lines:
    print(line.replace("\n",""))

# Create a dictionary to store names
name_count = {}

for name in lines:
    name = name.rstrip()
    # if name already in dictionary, add one to existing value
    if name in name_count:
        # Add 1
        current_value = name_count[name]
        # print("The current value for", name, "is", current_value)
        new_value = current_value + 1
        # print("The new value for", name, "is", new_value)
        name_count[name] = new_value
    # else, set value 1
    else:
        name_count[name] = 1

# Print out the updated dictionary
print(name_count)

# Write out to another file using file content manager
with open('final.txt', 'w') as task:
    for name in name_count:
        task.writelines(f'Name: {name}, Count: {name_count[name]}\n')
task.close()