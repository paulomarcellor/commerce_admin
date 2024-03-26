import sqlite3 as sql

def connectDB(db='commerce.db'):
    try:
        conn = sql.connect(db)
        cursor = conn.cursor()
        return conn, cursor
    except sql.Error as e:
        print(f"It was not possible to connect to database: {e}")
        return None, None

def closeDB(conn):
    if conn:
        try:
            conn.commit()
        except sql.Error as e:
            print(f"Commit error: {e}")
        finally:
            try:
                conn.close()
            except sql.Error as e:
                print(f": {e}")

def insertProductDB(product_name, product_category):
    insertProductQuery = """ INSERT INTO PRODUCTS (product_id, name, category) VALUES (?, ?, ?)"""
    
    conn = sql.connect(db)
    cursor = conn.cursor()

    product_id = int(cursor.execute(""" SELECT MAX(product_id) FROM PRODUCTS """).fetchone()[0])+1

    cursor.execute(insertProductQuery,(product_id, product_category, product_name))

    conn.commit()
    conn.close()
    return 'Product inserted'