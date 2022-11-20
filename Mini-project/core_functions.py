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

# def load_products():
    # Read products from products table

# def load_couriers():
    # Read couriers from courier table

def load_orders():
    # Read orders.csv file and update orders dictionary
    with open('Practice/orders.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            new_order = dict(row)
            orders.append(new_order)
    file.close()

# def save_products_list():
    # Write out to products table

# def save_courier_list():
    # Write out to courier table

def save_order_list():
    # Write to orders.csv file
    with open('Practice/orders.csv', mode='w') as csv_file:
        headers = ['customer_name', 'customer_address', 'customer_phone',
         'courier', 'order_status', 'items']
        writer = csv.DictWriter(csv_file, fieldnames = headers)

        writer.writeheader()
        for new_order in orders:
            writer.writerow(new_order)
    csv_file.close()

def create_product():
    try:
        product_name = input('Enter product name: ').title()
        price = float(input('Enter product price: '))
        new_product = {'name': product_name,
                'price': f'£{price}'}

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

def create_new_order():
    # Get user input to update orders dictionary
    customer_name = input('Enter customer name: ').title()
    customer_address = input('Enter customer address: ')
    customer_phone = input('Enter customer phone number: ')

    # PRINT product list with index value for each product
    products_list()

    # Taking multiple user inputs separated by comma
    item = input('Enter product index you wish to'
    ' add to order: ')
    items = str(item)
    print(items)

    # PRINT couriers list with index value for each courier
    courier_index_list()
    coury_index = input('Enter courier index: ') # courier index
    order_status = 'preparing'

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
    order_index = int(input("Select index for the order you wish to delete: "))
    # DELETE order at index in order list
    orders.remove(orders[order_index])

# load_products(), load_couriers(), load_orders()