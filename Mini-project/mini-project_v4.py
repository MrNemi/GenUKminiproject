# Import key modules for cafe ordering app
from functions.products_ import *
from functions.couriers_ import *
from functions.orders_ import *
from file_handling.csvfile_handling import *
 
# Display main menu
def main_menu():
    print("_________Welcome to Manny's___________\n"
        '\n*************Main menu****************\n'
        '0: Save data and exit app\n1: Product menu\n'
        '2: Couriers menu\n3: Orders menu\n')

# Load data from .csv files
load_products(), load_couriers(), load_orders()

# Main loop
while True:
    clear_screen()
    main_menu()
    try:
        # Get user input for main menu option
        val = int(input('Enter a number to access main menu: '))
        
        # If user input is 0, exit app
        if val == 0:
            save_products_list(), save_courier_list(), save_order_list()
            print('All data has been saved.\nExiting the app!!!')
            
            # Give user the option to log back into the app or exit fully.
            menu_continue = input("Return to main menu? (yes/no): ")
            if menu_continue != "yes" and menu_continue== "no":
                break
        
        # If user input is 1: Enter products menu
        elif val == 1:
            product_loop()

        # If user input is 2: Enter couriers menu
        elif val == 2:
            couriers_loop()

        # If user input is 3: Enter orders menu
        elif val == 3:
            orders_loop()

        else:
            print("Invalid input. Enter either 0, 1, 2, or 3")

    except ValueError as e:
        print(e)