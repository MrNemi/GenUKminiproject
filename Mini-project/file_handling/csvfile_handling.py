# Functions for reading and writing to 
# products, couriers, and orders.csv files

from functions.products_ import *
from functions.couriers_ import *
from functions.orders_ import *

# Import csv module
import csv

def load_products():
    # Read products.csv file and update products dictionary
    with open('Mini-project\data\products.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            new_product = dict(row)
            products.append(new_product)

def load_couriers():
    # Read couriers.csv file and update couriers dictionary
    with open('Mini-project\data\couriers.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            new_courier = dict(row)
            couriers.append(new_courier)

def load_orders():
        # Read orders.csv file and update orders dictionary
    with open('Mini-project\data\orders.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            new_order = dict(row)
            orders.append(new_order)

def save_products_list():
    # Write out to a csv file using file content manager
    with open('Mini-project\data\products.csv', mode='w') as csv_file:
        headers = ['name', 'price']
        writer = csv.DictWriter(csv_file, fieldnames = headers)
        writer.writeheader()
        for new_product in products:
            writer.writerow(new_product)

def save_courier_list():
    # Write out to a csv file using file content manager
    with open('Mini-project\data\couriers.csv', mode='w') as csv_file:
        headers = ['name', 'phone']
        writer = csv.DictWriter(csv_file, fieldnames = headers)
        writer.writeheader()
        for new_courier in couriers:
            writer.writerow(new_courier)

def save_order_list():
    # Write to orders.csv file
    with open('Mini-project\data\orders.csv', mode='w') as csv_file:
        headers = ['customer_name', 'customer_address', 'customer_phone',
         'courier', 'order_status', 'items']
        writer = csv.DictWriter(csv_file, fieldnames = headers)

        writer.writeheader()
        for new_order in orders:
            writer.writerow(new_order)