# Mini-project User Interface
print("Welcome to Manny's")

# Create products list
products = ['burgers', 'nachos', 'pizza','fries', 'gyros','wraps']

# Functions
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

while True:
    # Get user input for main menu option
    val = int(input('Enter a number to access menu: '))
    
    if val in (0, 1):

        # If user input is 0, exit app
        if val == 0:
            print('You have logged out of the app.')

        # If user input is 1:
        elif val == 1:
            # print product menu options
            print('Products menu:')
            for product in products:
                print(product)
            
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
                    
                    submenu_continue = input("Continue? (yes/no): ")
                    if submenu_continue == "no":
                        break

                else:
                    print("Wrong input. Enter a value from 0 to 4")
        
        menu_continue = input("Would you like to proceed? (yes/no): ")
        if menu_continue == "no":
          break

    else:
        print("Invalid input. Enter either a 0 or 1")