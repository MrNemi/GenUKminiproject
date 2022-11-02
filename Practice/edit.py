temp_type = input('Enter either c for celsius or f for fahrenheit: ').lower()
while temp_type != 'c' and temp_type != 'f':
    temp_type = input('Enter either c for celsius or f for fahrenheit').lower()
    break
temp_value = int(input('Enter a number'))
while temp_value:
    temp = int(input('Enter a number'))
    break
if temp_type == 'c':
    temp_fah_value = (temp_value * 1.8) + 32
    print(f'{temp_value}{temp_type} is {temp_fah_value}f')
elif temp_type == 'f':
    temp_cel_value = (temp_value -32)*(5/9)
    print(f'{temp_value}{temp_type} is {temp_cel_value}c')