# Empty products dictionary
products = []
new_product = {}

def product_menu():
    print('*************Product menu*************')
    print('[0]: Return to main menu\n[1]: Print products list\n'
        '[2]: Create new product\n[3]: Update existing product\n'
        '[4]: Delete a product\n')

def create_product():
    try:
        product_name = input('Enter product name: ').title()
        price = float(input('Enter product price: '))
        new_product = {'name': product_name,
                'price': price}

        products.append(new_product)
        print(products)
    except Exception as e:
        print(e)
        print("Enter valid input.")

def view_products():
    # printing out the products
    print("\nProducts available:\n")
    for product in products:
        item = list(product.values())
        print(item,'\n')

def product_index():
    # PRINT product list with its index values
    print("\nProducts List:\n")
    i = 0
    for new_product in products:
        print(f"Product: {new_product}\nIndex: {i}\n")
        i += 1

def update_product():
    # PRINT product list with its index values
    product_index()
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

def product_loop():
    # print product menu options
    product_menu()
    while True:
        try:
            #  Get user input for product menu option
            var = int(input('Enter a number to access product menu: '))
            if var in range(0, 5):
                #  If user input is 0: Return to main menu
                if var == 0:
                    break
                
                #  If user input is 1, print products list
                elif var == 1:
                    view_products()

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