# Purchase-Analytics

This is my solution for Insight Data Engineering coding challenge.

## There are three steps to solve the problems:
(1) Create a production id to department id mapping.
  
  In this step, products.csv is read in and a Python Dict is created from it: {key: product_id, value: department_id}

(2) Count the number of order and number of first order.

  In this step, I use a Python Dict to save the result:
  
  {key: department_id, value: {key: number_of_order, value: int, key: number_of_first_order, value: int}

  Order_products.csv is read in and is processed line by line. For each order, department_id is abtained from product_id using the production id to department id mapping. Then the field number_of_order and number_of_first_order (if it is the first time order) in the result Dict is increased by 1.

(3) write the result to output csv file.
