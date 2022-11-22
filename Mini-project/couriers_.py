# Empty couriers dictionary
couriers = []
new_courier = {}

def couriers_menu():
    print('*************Couriers menu*************')
    print('(0): Return to main menu\n(1): Print couriers list\n'
        '(2): Create new courier\n(3): Update existing courier\n'
        '(4): Delete a courier\n')

def couriers_list():
    # printing out the couriers list
    print("\nCouriers available:\n")
    for courier in couriers:
        print(courier)
    print("\n")

def new_couriers():
    # Get user input to update couriers list
    courier_name = input('Enter courier name: ').title()
    mobile_no = input('Enter courier phone number: ')
    new_courier = {'name': courier_name,
            'phone': mobile_no}
    couriers.append(new_courier)

    # printing all the couriers
    couriers_list()

def courier_index_list():
    # PRINT courier name with its index values
    print("\nCouriers List:\n")
    i = 0
    for courier in couriers:
        print(f"Courier: {courier}, Index: {i}\n")
        i += 1

def update_courier():
    courier_index_list()
    # GET user input for courier index value
    courier_index = int(input("Select index for the courier you wish to update: "))
    print(couriers[courier_index])
    change = couriers[courier_index]

    # FOR EACH key-value pair in selected order:
    for key, value in change.items():
        print(f"Key: {key}, Value: {value}")
        # GET user input for updated property
        update = input("Enter new value or press enter to continue: ")
        # If user input is blank, do not update this property
        if update.strip() == '':
            continue
        # Else, update the property value with user input
        else:
            change[key] = update

def delete_courier():
    courier_index_list()
    # get user input for courier index value
    unit = int(input('Enter index value for courier to be deleted: '))
    # delete courier dict at index in products list
    couriers.pop(unit)
    print(couriers)

def couriers_loop():
    # print courier menu options
    couriers_menu()
    while True:
        try:
            #  Get user input for couriers menu option
            coury = int(input('Enter a number to access couriers menu: '))

            for coury in range(0, 5):
                #  If user input is 0:
                if coury == 0:
                #  Return to main menu
                    break
                
                #  If user input is 1, print couriers list
                elif coury == 1:
                    couriers_list()

                #  If user input is 2, create new courier dict
                #  and append to couriers list.
                elif coury == 2:
                    new_couriers()

                #  If user input is 3, update existing courier
                elif coury == 3:
                    update_courier()
                
                #  If user input is 4, delete courier
                elif coury == 4:
                    delete_courier()
                
                couriers_continue = input("Remain on the courier menu? (yes/no): ")
                if couriers_continue == "no":
                    break

            else:
                print("Wrong input. Enter a value from 0 to 5")

        except Exception as e:
            print(e)
            print("Enter valid input.")