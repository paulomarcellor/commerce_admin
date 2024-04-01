import sqlite3 as sql

createProductsTable = """

    CREATE TABLE PRODUCTS (
        product_id INTEGER PRIMARY KEY,
        name VARCHAR(200),
        category VARCHAR(100),
        cost DECIMAL(10, 2),
        price DECIMAL(10, 2),
        amount INTEGER
    );

"""

createClientsTable = """

    CREATE TABLE CLIENTS (
        client_id INTEGER PRIMARY KEY,
        name VARCHAR(200),
        age INTEGER,
        marital_status VARCHAR(20),
        email VARCHAR(100),
        phone VARCHAR(20),
        occupation VARCHAR(100),
        preferencial_communication VARCHAR(100),
        location VARCHAR(100),
        average_ticket DECIMAL(10, 2)      
    );

"""


createStockTable = """

    CREATE TABLE STOCK (
        product_id INTEGER,
        date_in DATE,
        amount INTEGER,
        FOREIGN KEY (product_id) REFERENCES PRODUCTS(product_id)
    );


"""

createSalesTable = """

    CREATE TABLE SALES (
        transaction_id INTEGER PRIMARY KEY,
        sale_date DATE,
        client_id INTEGER,
        product_id INTEGER,
        sold_products VARCHAR(255),
        quantity_sold INTEGER,
        unit_price DECIMAL(10, 2),
        total_price DECIMAL(10, 2),
        discounts DECIMAL(10, 2),
        additional_fees DECIMAL(10, 2),
        payment_method VARCHAR(50),
        transaction_status VARCHAR(50),
        delivery_method VARCHAR(50),
        employee_id INTEGER,
        sale_location VARCHAR(100),
        coupon_code_used VARCHAR(50),
        additional_notes TEXT,
        FOREIGN KEY (client_id, product_id) REFERENCES PRODUCTS(client_id, product_id)
        );

"""

conn = sql.connect('commerce.db')
cursor = conn.cursor()

cursor.execute(createProductsTable)
cursor.execute(createClientsTable)
cursor.execute(createStockTable)
cursor.execute(createSalesTable)

conn.commit()
conn.close()