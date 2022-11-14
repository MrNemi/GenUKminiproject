

# Empty products dictionary
products = []
new_product = {}

# Empty couriers dictionary
couriers = []
new_courier = {}

# CREATE orders list of dictionaries
orders = []
new_order = {}

# CREATE order status list
order_status_list = ["Preparing", "Awaiting Pickup", "Out for Delivery", "Delivered"]

# Import csv module
import csv

# Core Functions
def main_menu():
    print("Welcome to Manny's :)\n"
        '*************Main menu*************\n'
        '0: Save data and exit app\n1: Product menu\n'
        '2: Couriers menu\n3: Orders menu\n')

def product_menu():
    print('*************Product menu*************')
    print('[0]: Return to main menu\n[1]: Print products list\n'
        '[2]: Create new product\n[3]: Update existing product\n'
        '[4]: Delete a product\n')

def couriers_menu():
    print('*************Couriers menu*************')
    print('(0): Return to main menu\n(1): Print couriers list\n'
        '(2): Create new courier\n(3): Update existing courier\n'
        '(4): Delete a courier\n')

def orders_menu():
    print('*************Orders menu*************')
    print('[0]: Return to main menu\n[1]: Print orders list\n'
        '[2]: Create new order\n[3]: Update existing order status\n'
        '[4]: Update existing order\n[5]: Delete an order\n')

def load_products():
    # Read products.csv file and update products dictionary
    with open('Practice/products.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            new_product = dict(row)
            products.append(new_product)
    file.close()
    # print(products)

def load_couriers():
    # Read couriers.csv file and update couriers dictionary
    with open('Practice/couriers.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            new_courier = dict(row)
            couriers.append(new_courier)
    file.close()

#def load_orders():

def save_products_list():
    # Write out to a csv file using file content manager
    with open('Practice/products.csv', mode='w') as csv_file:
        headers = ['Name', 'Price']
        writer = csv.DictWriter(csv_file, fieldnames = headers, delimiter = '\t')
        writer.writeheader()
        for new_product in products:
            writer.writerow(new_product)
    csv_file.close()

def save_courier_list():
    # Write out to a csv file using file content manager
    with open('Practice/couriers.csv', mode='w') as csv_file:
        fields = ['Name', 'Phone']
        writer = csv.DictWriter(csv_file, fieldnames = fields)
        writer.writeheader()
        for new_courier in couriers:
            writer.writerow(new_courier)
    csv_file.close()

def save_order_list():
    # Write to orders.csv file
    with open('Practice/orders.csv', mode='a') as csv_file:
        headers = ['customer_name', 'customer_address', 'customer_phone',
         'courier', 'order_status', 'items']
        writer = csv.DictWriter(csv_file, fieldnames = headers, delimiter = '\t')

        writer.writeheader()
        for new_order in orders:
            writer.writerow(new_order)

def create_product():
    try:
        product_name = input('Enter product name: ').title()
        price = float(input('Enter product price: '))
        new_product = {'Name': product_name,
                'Price': '£' + price}

        products.append(new_product)
        print(products)
    except Exception as e:
        print(e)
        print("Enter valid input.")

def products_list():
    # PRINT product list with its index values
    print("\nProducts List:\n")
    i = 0
    for new_product in products:
        print(f"Product: {new_product}\nIndex: {i}\n")
        i += 1

def update_product():
    # PRINT product list with its index values
    products_list()
    # GET user input for product index value
    prod_index = int(input("Select index for the product you wish to update: "))
    print(products[prod_index])
    edit = products[prod_index]

    # FOR EACH key-value pair in selected order:
    for key, value in edit.items():
        print(f"Key: {key}, Value: {value}")
        # GET user input for updated property
        update = input("Enter new value or press enter to continue: ")
        # If user input is blank, do not update this property
        if update.strip() == '':
            continue
        # Else, update the property value with user input
        else:
            edit[key] = update

def delete_product():
    # print products list and index
    for i in range(len(products)):
        print(list((products[i], i)))
    # get user input for product index value
    num = int(input('Enter index value for product to be deleted: '))
    # delete product dictionary at index in products list
    products.pop(num)
    print(products)

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
    new_courier = {'Name': courier_name,
            'Phone': mobile_no}
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

def create_new_order():
    # Get user input to update orders dictionary
    customer_name = input('Enter customer name: ').title()
    customer_address = input('Enter customer address: ')
    customer_phone = input('Enter customer phone number: ')

    # PRINT couriers list with index value for each courier
    couriers_list()
    coury_index = input('Enter courier index: ') # courier index
    order_status = 'preparing'

    # PRINT product list with index value for each product
    products_list()
    items = input('Enter product index you wish to'
            ' add to order: ') # Product index

    new_order = {'customer_name': customer_name,
                'customer_address': customer_address,
                'customer_phone': customer_phone,
                'courier': coury_index,
                'order_status': order_status,
                'items': items}
    orders.append(new_order)

    # printing all the orders
    print("\nOrders List:\n")
    for order in orders:
        print(order)
    print("\n")

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

load_products(), load_couriers(),#load_orders()
 
while True:
    main_menu()
    # Get user input for main menu option
    val = int(input('Enter a number to access main menu: '))
    
    if val in (0, 1, 2, 3):
        # If user input is 0, exit app
        if val == 0:
            save_products_list(), save_courier_list(), save_order_list()
            print('All data has been saved.\nLog out successful!!!')
        
        # Products menu
        # If user input is 1:
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
                            main_menu()
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

        # Couriers menu
        # If user input is 2:
        elif val == 2:
            # print courier menu options
            couriers_menu()

            while True:
                #  Get user input for couriers menu option
                coury = int(input('Enter a number to access couriers menu: '))

                if coury in (0, 1, 2, 3, 4):
                    #  If user input is 0:
                    if coury == 0:
                    #  Return to main menu
                        main_menu()
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

        # Orders menu
        # If user input is 3:
        elif val == 3:
            # print orders menu
            orders_menu()

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
                    
                    orders_continue = input("Still ordering? (yes/no): ")
                    if orders_continue == "no":
                        break

                else:
                    print("Wrong input. Enter a value from 0 to 5")
        
        menu_continue = input("Proceed to the main menu? (yes/no): ")
        if menu_continue == "no":
          break

    else:
        print("Invalid input. Enter either a 0 or 1")