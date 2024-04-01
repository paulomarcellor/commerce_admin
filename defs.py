import sqlite3 as sql

def database(db,query,fields):
    conn = sql.connect(db)
    cursor = conn.cursor()
    cursor.execute(query, fields)
    conn.commit()
    conn.close()

def insertProductDB(product_name, product_category, product_cost, product_price):
    insertProductQuery = """ INSERT INTO PRODUCTS (name, category, cost, price) VALUES (?, ?, ?, ?)"""
    fields = product_name, product_category, product_cost, product_price
    database('commerce.db',insertProductQuery, fields)
    return 'Registered product'

def insertClientDB(client_name, client_age, client_marital_status,\
                   client_email, client_phone, client_occupation, client_preferencial_communication,\
                    client_location):
    insertClientQuery = """ INSERT INTO CLIENTS (name, age, marital_status,\
                   email, phone, occupation, preferencial_communication,\
                    location, average_ticket) VALUES (?,?,?,?,?,?,?,?,?)"""
    database('commerce.db',insertClientQuery, fields)
    return 'Registered client'

def insertSaleDB(sale_date,client_id,product_id,sold_products,quantity_sold,unit_price,total_price,\
                 discounts,additional_fees,payment_method,transaction_status,delivery_method,employee_id,\
                sale_location,coupon_code_used,additional_notes):
    
    insertSaleQuery = """INSERT INTO SALES (sale_date,client_id,product_id,sold_products,quantity_sold,unit_price,total_price,\
                 discounts,additional_fees,payment_method,transaction_status,delivery_method,employee_id,\
                sale_location,coupon_code_used,additional_notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    
    database('commerce.db',insertSaleQuery, fields)
    
    return 'Registered sale'
    