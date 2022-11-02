# 1. Add a new key-value pair to the below car dictionary for the colour. 
# Print out the colour to verify it worked.
# 2. Update the value of the model in the car dictionary. 
# Print out the new value to verify it worked.
# 3. Delete the model key-pair from the car dictionary. 
# Print out the entire dictionary to verify it worked.
# 4. Use the items() function to loop through the dictionary 
# and print each key-value pair like so:  key: x, value: y

# Hint: for key, value in x.items(): Hint: You will need to cast the values to a string

car = {
 'brand': 'Ford',
 'model': 'Mustang',
 'year' : 1964,
 'isNew': False
}

#Task 1
# car['colour'] = 'blue'
# print(car.get('colour'))

#Task 2
# car['model'] = 'Ferrari'
# print(car.get('model'))

#Task 3
# del car['model']
# print(car)

#Task 4
for item in car.items():
    print(f'{item}')