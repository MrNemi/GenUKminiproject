# Import key modules for cafe ordering app
from products_ import *
from couriers_ import *
from orders_ import *
from csvfile_handling import *

# Core Functions
def main_menu():
    print("Welcome to Manny's :)\n"
        '*************Main menu*************\n'
        '0: Save data and exit app\n1: Product menu\n'
        '2: Couriers menu\n3: Orders menu\n')

# Load data from .csv files
load_products(), load_couriers(), load_orders()

# Main loop
while True:
    main_menu()
    try:
        # Get user input for main menu option
        val = int(input('Enter a number to access main menu: '))
        
        # If user input is 0, exit app
        if val == 0:
            save_products_list(), save_courier_list(), save_order_list()
            print('All data has been saved.\nExiting the app!!!')
        
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

        menu_continue = input("Proceed to the main menu? (yes/no): ")
        if menu_continue == "no":
            break

    except ValueError as e:
        print(e)