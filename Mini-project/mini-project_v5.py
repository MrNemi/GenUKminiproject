# Import core functions for cafe ordering app
from core_functions import *

# Main program
while True:
    main_menu()

    try:
        # Get user input for main menu option
        val = int(input('Enter a number to access main menu: '))
        
        if val in (0, 1, 2, 3):
            # If user input is 0, exit app
            if val == 0:
                # save_order_list()
                print('All data has been saved.\nLog out successful!!!')
            
            # If user input is 1: Products menu
            elif val == 1:
                # product menu main loop
                product_loop()

            # If user input is 2: Couriers menu
            elif val == 2:
                # couriers menu main loop
                couriers_loop()

            # If user input is 3: Orders menu
            elif val == 3:
                # orders menu main loop
                orders_loop()
            
            menu_continue = input("Proceed to the main menu? (yes/no): ")
            if menu_continue == "no":
                break
        else:
            print("Enter a number between 0 to 3")

    except ValueError as e:
        print(e)
        print("Enter a valid input")
    except IndexError as e:
        print(e)
        print("Enter a valid input")