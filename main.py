### NEXT STEPS:
# Fix field "total_profit" from SALES

import streamlit as st
import sqlite3 as sql
import pandas as pd
import defs

st.set_page_config(page_title="Commerce Admin", layout="wide", initial_sidebar_state="auto")
st.title('Commerce Administration')

# DB Connect
conn = sql.connect('commerce.db')

# DATA CLIENTS

clients_names = pd.read_sql_query('select name, client_id from clients', conn)
clients_ids_names = [f"{client_id} - {name}" for name, client_id in zip(clients_names['name'], clients_names['client_id'])]

products = pd.read_sql_query('select * from products', conn)
products_ids_names = [f"{product_id} - {name}" for name, product_id in zip(products['name'], products['product_id'])]

# DB Close
conn.close()

# DATA INSERT

with st.sidebar:
    st.title('Sidebar')
    st.text('Sidebar')

tab1, tab2, tab3 = st.tabs(['Dashboard','Raw Data','Management'])

with tab2:
    st.dataframe(products)

# MANAGEMENT
with tab3:
    st.header('Management System')
    col31, col32, col33 = st.columns(3)
    with col31:
        # Sales Form
        with st.form("Register Sale", clear_on_submit=False):
            st.header('Register Sale')
            sale_date = st.date_input('Data')
            client = st.selectbox('Client', clients_ids_names)
            if client:
                client_id = client.split(' - ')[0]
            product = st.selectbox('Products', products_ids_names)
            if product:
                product_id = product.split(' - ')[0]
            quantity_sold = st.number_input('Amount', value=None)
            discounts = st.number_input('Discounts', value=None)
            additional_fees = st.number_input('Additional Fees', value=None)
            payment_method = st.selectbox('Payment Method', ['Cash', 'Card', 'Other'])
            transaction_status = st.selectbox('Status', ['Done','Waiting for Payment'])
            delivery_method = st.selectbox('Delivery Method', ['Store', 'Delivery'])
            employee_id = st.selectbox('Seller', ['1 - Mary','2 - Joseph','3 - Paul'])
            sale_location = st.selectbox('Storage',['Malibu', 'Silicon Valley', 'Central'])
            total_price = (products[products['product_id']==product_id]['price']*products[products['product_id']==product_id]['amount'])-discounts+additional_fees
            total_profit = total_price-(products[products['product_id']==product_id]['cost']*products[products['product_id']==product_id]['amount'])
            sendSale = st.form_submit_button("Register")
        if sendSale:
            defs.insertSaleDB(sale_date=sale_date,client_id=client_id,product_id=product_id,quantity_sold=quantity_sold,total_price=total_price,\
                 discounts=discounts,additional_fees=additional_fees,payment_method=payment_method,transaction_status=transaction_status,delivery_method=delivery_method,employee_id=employee_id,\
                sale_location=sale_location, total_profit=total_profit)
            st.success('Success!')
    with col32:
        # Clients Form
        with st.form("Register Client", clear_on_submit=False):
            st.header('Register Client')
            client_name=st.text_input('Name')
            client_age=st.number_input('Age', value=None)
            client_marital_status=st.selectbox('Marital Status', ['Single','Married', 'Divorced', 'Widowed'])
            client_email=st.text_input('E-mail')
            client_phone=st.text_input('Phone Number')
            client_occupation=st.text_input('Occupation')
            client_preferencial_communication=st.selectbox('Preferencial Communication', ['Phone', 'SMS', 'E-mail'])
            client_location=st.text_input('Location')
            sendClient = st.form_submit_button('Register')
        if sendClient:
            defs.insertClientDB(client_name, client_age, client_marital_status,\
                   client_email, client_phone, client_occupation, client_preferencial_communication,\
                    client_location)
            st.success(str(client_name) + ' Registered Successfully')
        
    with col33:
        # Products Form
        with st.form("Register Product", clear_on_submit=True):
            st.header('Register Product')
            name = st.text_input("Name")
            category = st.text_input("Category")
            cost = st.number_input('Cost')
            price=st.number_input('Price')
            sendProduct = st.form_submit_button("Register")
        if sendProduct:
            defs.insertProductDB(product_name=name, product_category=category, product_cost=cost, product_price=price)
            st.success('Success!')

            
    