# CREATE orders list of dictionaries
orders = []
new_order = {}

# CREATE order status list
order_status_list = ["Preparing", "Awaiting Pickup", "Out for Delivery", "Delivered"]

from products_ import product_index
from couriers_ import courier_index_list

def orders_menu():
    print('*************Orders menu*************')
    print('[0]: Return to main menu\n[1]: Print orders list\n'
        '[2]: Create new order\n[3]: Update existing order status\n'
        '[4]: Update existing order\n[5]: Delete an order\n')

def create_new_order():
    # Get user input to update orders dictionary
    customer_name = input('Enter customer name: ').title()
    customer_address = input('Enter customer address: ')
    customer_phone = input('Enter customer phone number: ')

    # PRINT product list with index value for each product
    product_index()

    # Taking multiple user inputs separated by comma
    item = input('Enter product index you wish to'
    ' add to order: ')
    items = str(item)
    print(items)

    # PRINT couriers list with index value for each courier
    courier_index_list()
    coury_index = input('Enter courier index: ') # courier index
    order_status = order_status_list[0]

    new_order = {'customer_name': customer_name,
                'customer_address': customer_address,
                'customer_phone': customer_phone,
                'courier': coury_index,
                'order_status': order_status,
                'items': items}
    orders.append(new_order)

    # printing all the orders
    print("\nOrders List:\n", orders)

def orders_list():
    # PRINT orders list with its index values
    print("\nOrders List:\n")
    i = 0
    j = 1
    for order in orders:
        print(f"Order {j}: {order}\nIndex: {i}\n")
        i += 1
        j += 1

def orders_view():
    print("How would you like to view your orders?")
    try:
        format = input("Enter 'c' for list by couriers or 's'"
                    " for list by order status: ").title()
        if format == 'C':
            # using sorted and lambda to print list of orders sorted by courier
            sort_orders = sorted(orders, key=lambda i: i['courier'])
            # print out the sorted orders
            print("Orders list sorted by couriers:\n")
            # Iterating over all the values of the orders dictionary
            i = 1
            for item in sort_orders:
                items = list(item.values())
                print(f"Order {i}:\n {items},\n")
                i += 1

        elif format == 'S':
            # using sorted and lambda to print list of 
            # orders sorted by order status
            sort_orders = sorted(orders, key=lambda i: i['order_status'])
            # print out the sorted orders
            print("Orders list sorted by status:\n")
            # Iterating over all the values of the orders dictionary
            i = 1
            for item in sort_orders:
                items = list(item.values())
                print(f"Order {i}:\n {items},\n")
                i += 1

    except Exception as e:
        print(e)

def update_order_status():
    orders_list()
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
    orders_list()
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
    orders_list()
    # GET user input for order index value
    order_index = int(input("Select index for the order you wish to delete: "))
    # DELETE order at index in order list
    orders.remove(orders[order_index])

def orders_loop():
    # print orders menu
    orders_menu()
    while True:
        try:
            #  Get user input for orders menu option
            num = int(input('Enter a number to access orders menu: '))
            if num in range(0, 6):
                #  If user input is 0:
                if num == 0:
                #  Return to main menu
                    break
                
                #  If user input is 1, print orders dictionary
                elif num == 1:
                    orders_view()
                    # print(f'Orders List:\n{orders}')

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
                
                orders_continue = input("Still ordering? (yes/no): ")
                if orders_continue == "no":
                    break
            else:
                print("Wrong input. Enter a value from 0 to 5")

        except Exception as e:
            print(e)
            print("Enter valid input.")