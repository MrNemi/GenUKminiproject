# Import core functions for cafe ordering app
from core_functions import *

# Main program
while True:
    main_menu()
    # Get user input for main menu option
    val = int(input('Enter a number to access main menu: '))
    if val in (0, 1, 2, 3):
        # If user input is 0, exit app
        if val == 0:
            # save_order_list()
            print('All data has been saved.\nLog out successful!!!')
        
        # If user input is 1: Products menu
        elif val == 1:
            # print product menu options
            product_menu()
            
            while True:
                try:
                    #  Get user input for product menu option
                    var = int(input('Enter a number to access product menu: '))

                    if var in (0, 1, 2, 3, 4):
                        #  If user input is 0:
                        if var == 0:
                        #  Return to main menu
                            break
                        
                        #  If user input is 1, print products list
                        elif var == 1:
                            print(products)

                        #  If user input is 2, create new product
                        elif var == 2:
                            create_product()

                        # If user input is 3, update existing product
                        elif var == 3:
                        # using list comprehension to print product names and index value
                            update_product()

                        # If user input is 4, delete a product
                        elif var == 4:
                            delete_product()
                        
                        products_continue = input("Remain on the products menu? (yes/no): ")
                        if products_continue == "no":
                            break
                    else:
                        print("Wrong input. Enter a value from 0 to 4")

                except Exception as e:
                    print(e)
                    print("Enter valid input.")

        # If user input is 2: Couriers menu
        elif val == 2:
            # print courier menu options
            couriers_menu()

            while True:
                try:
                    #  Get user input for couriers menu option
                    coury = int(input('Enter a number to access couriers menu: '))

                    if coury in (0, 1, 2, 3, 4):
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

        # If user input is 3: Orders menu
        elif val == 3:
            # print orders menu
            orders_menu()

            while True:
                try:
                    #  Get user input for orders menu option
                    num = int(input('Enter a number to access orders menu: '))

                    if num in (0, 1, 2, 3, 4, 5):
                        #  If user input is 0:
                        if num == 0:
                        #  Return to main menu
                            break
                        
                        #  If user input is 1, print orders dictionary
                        elif num == 1:
                            print(f'Orders List:\n{orders}')

                        #  If user input is 2, create new order and append to orders list.
                        elif num == 2:
                            create_new_order()

                        #  If user input is 3, update existing order status
                        elif num == 3:
                            update_order_status()
                        
                        #  If user input is 4, update order
                        elif num == 4:
                            update_order()
                        
                        #  If user input is 5, delete order
                        elif num == 5:
                            delete_order()
                            print(f'Orders List:\n{orders}')
                        
                        orders_continue = input("Still ordering? (yes/no): ")
                        if orders_continue == "no":
                            break

                    else:
                        print("Wrong input. Enter a value from 0 to 5")
                except Exception as e:
                    print(e)
                    print("Enter valid input.")
        
        menu_continue = input("Proceed to the main menu? (yes/no): ")
        if menu_continue == "no":
          break

    else:
        print("Invalid input. Enter either 0, 1, 2, or 3")