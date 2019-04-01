import csv
import sys

order_products_filename = sys.argv[1]
product_filename = sys.argv[2]
report_filename = sys.argv[3]

# Read product.csv and create a Dict to map product_id to department_id.
product_to_department_mapping = {}
with open(product_filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        product_id = row['product_id']
        department_id = int(row['department_id'])
        if product_id not in product_to_department_mapping:
            product_to_department_mapping[product_id] = department_id

# Read order_products.csv and count and number of orders and number of first orders.
report = {}
with open(order_products_filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        product_id = row['product_id']
        department_id = product_to_department_mapping[product_id]
        if department_id not in report:
            report[department_id] = {'number_of_orders': 0, 'number_of_first_orders': 0}
        report[department_id]['number_of_orders'] += 1
        if row['reordered'] == '0':
            report[department_id]['number_of_first_orders'] += 1

# Write the result to output file.
department_list = list(report.keys())
department_list.sort()
with open(report_filename, mode='w') as csv_file:
    fieldnames = ['department_id', 'number_of_orders', 'number_of_first_orders', 'percentage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for department_id in department_list:
        number_of_orders = report[department_id]['number_of_orders']
        number_of_first_orders = report[department_id]['number_of_first_orders']
        percentage = '%.2f' % ((number_of_first_orders + 0.0) / number_of_orders)
        writer.writerow({'department_id': department_id, 'number_of_orders': number_of_orders,
                        'number_of_first_orders': number_of_first_orders, 'percentage': percentage})