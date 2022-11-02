print("Welcome to Manny's :)")

# Create products list
products = ['burgers', 'nachos', 'pizza','fries', 'gyros','wraps']

# Create empty orders list and nested orders dictionary
orders = []
new_order = {}

# Core Functions
def main_menu():
    print('Main menu options:')
    for product in products:
        print(product)

def create_product():
    #  Get user input for product name
    new = input('Enter a new product: ')
    #  Append product name to products list
    products.append(new)
    for product in products:
        print(product) 

def update_product():
    # using list comprehension to print product names with its index value
    for i in range(len(products)):
        print (list((products[i], i)))
    #  GET user input for product index value
    num = int(input('Enter index value for product to be updated: '))
    #  GET user input for new product name
    new = input('Enter a new product: ')
    #  UPDATE product name at index in products list
    products[num] = new
    print(products)

def delete_product():
    # print products list and index
    for i in range(len(products)):
        print(list((products[i], i)))
    # get user input for product index value
    num = int(input('Enter index value for product to be deleted: '))
    # delete product at index in products list
    products.pop(num)
    print(products)

def create_new_order():
    # Get user input to update orders dictionary
    customer_name = input('Enter customer name: ')
    customer_address = input('Enter customer address: ')
    customer_phone = input('Enter customer phone number: ')
    order_status = 'PREPARING'
    new_order = {'customer_name': customer_name,
                'customer_address': customer_address,
                'customer_phone': customer_phone,
                'order_status': order_status}
    orders.append(new_order)

    # printing all the orders
    print("\nOrders List:\n")
    for order in orders:
        print(order)
    print("\n")

    # Write out to a text file using file content manager
    with open('Practice\Orders.txt', 'w') as orderlist:
        orderlist.writelines(f'Order list: {orders}\n')
    orderlist.close()

def order_list():
    # PRINT orders list with its index values
    print("\nOrders List:\n")
    i = 0
    for order in orders:
        print(f"Order: {order}\nIndex: {i}\n")
        i += 1

def update_order_status():
    order_list()
    # GET user input for order index value
    order_index = int(input("Select index for the order you wish to update: "))
    print(orders[order_index])

    # PRINT order status list with index values
    order_status_list = ["Preparing", "Awaiting Pickup", "Out for Delivery", "Delivered"]
    count = 0
    for status in order_status_list:
        print(f"Status: {status}, Index: {count}")
        count += 1
    
    # GET user input for order status index value
    status_index = int(input('Choose status index you wish to update: '))
    # UPDATE status for order
    orders[order_index]["order_status"] = order_status_list[status_index]
    print(orders[order_index])

def update_order():
    order_list()
    # GET user input for order index value
    order_index = int(input("Select index for the order you wish to update: "))
    print(orders[order_index])
    print("\n")
    order = orders[order_index]
    # FOR EACH key-value pair in selected order:
    for key, value in order.items():
        print(f"Key: {key}, Value: {value}")
        # GET user input for updated property
        update = input("Enter new value or press enter to continue: ")
        # If user input is blank, do not update this property
        if update.strip() == '':
            continue
        # Else, update the property value with user input
        else:
            order[key] = update

def delete_order():
    order_list()
    # GET user input for order index value
    order_index = int(input("Select index for the order you wish to update: "))
    # DELETE order at index in order list
    orders.remove(orders[order_index])

while True:
    # Get user input for main menu option
    val = int(input('Enter a number to access menu: '))
    
    if val in (0, 1, 2):
        # If user input is 0, exit app
        if val == 0:
            print('You have logged out of the app.')
        
        # Products menu
        # If user input is 1:
        elif val == 1:
            # print product menu options
            print('Products List:')
            for product in products:
                print(product.title())
            
            while True:
                #  Get user input for product menu option
                var = int(input('Enter a number to access product menu: '))

                if var in (0, 1, 2, 3, 4):
                    #  If user input is 0:
                    if var == 0:
                    #  Return to main menu
                        main_menu()
                    
                    #  If user input is 1, print products list
                    elif var == 1:
                        print(products.title())

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
                    
                    products_continue = input("Continue? (yes/no): ")
                    if products_continue == "no":
                        break
                else:
                    print("Wrong input. Enter a value from 0 to 4")

        # Orders menu
        # If user input is 2:
        elif val == 2:
            while True:
                #  Get user input for orders menu option
                num = int(input('Enter a number to access orders menu: '))

                if num in (0, 1, 2, 3, 4, 5):
                    #  If user input is 0:
                    if num == 0:
                    #  Return to main menu
                        main_menu()
                    
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
                    
                    orders_continue = input("Continue? (yes/no): ")
                    if orders_continue == "no":
                        break

                else:
                    print("Wrong input. Enter a value from 0 to 5")
        
        menu_continue = input("Would you like to proceed? (yes/no): ")
        if menu_continue == "no":
          break

    else:
        print("Invalid input. Enter either a 0 or 1")