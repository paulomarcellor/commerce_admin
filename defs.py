import sqlite3 as sql

def insertProductDB(product_name, product_category):
    insertProductQuery = """ INSERT INTO PRODUCTS (product_id, name, category) VALUES (?, ?, ?)"""
    conn = sql.connect('commerce.db')
    cursor = conn.cursor()
    if cursor.execute(""" SELECT MAX(product_id) FROM PRODUCTS """).fetchall()[0][0] == None:
        product_id = 0
    else:
        print(cursor.execute(""" SELECT MAX(product_id) FROM PRODUCTS """).fetchall()[0][0])
        product_id = int(cursor.execute(""" SELECT MAX(product_id) FROM PRODUCTS """).fetchall()[0][0])+1
    cursor.execute(insertProductQuery,(product_id,product_name,product_category))
    conn.commit()
    conn.close()
    return 'Registered product'

def insertClientDB(client_name, client_age, client_marital_status,\
                   client_email, client_phone, client_occupation, client_preferencial_communication,\
                    client_location):
    insertClientQuery = """ INSERT INTO CLIENTS (client_id, name, age, marital_status,\
                   email, phone, occupation, preferencial_communication,\
                    location, average_ticket) VALUES (?,?,?,?,?,?,?,?,?,?)"""
    conn = sql.connect('commerce.db')
    cursor = conn.cursor()
    if cursor.execute(""" SELECT MAX(client_id) FROM CLIENTS """).fetchall()[0][0] == None:
        client_id = 0
    else:
        print(cursor.execute(""" SELECT MAX(product_id) FROM CLIENTS """).fetchall()[0][0])
        client_id = int(cursor.execute(""" SELECT MAX(product_id) FROM CLIENTS """).fetchall()[0][0])+1
    average_ticket = 0
    cursor.execute(insertClientQuery,(client_id, client_name, client_age, client_sex, client_marital_status,\
                   client_email, client_phone, client_occupation, client_preferencial_communication,\
                    client_location, average_ticket))
    conn.commit()
    conn.close()
    return 'Registered client'