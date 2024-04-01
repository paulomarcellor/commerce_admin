### NEXT STEPS:
# Create column "Profit"
# Finish selling insert

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

pruducts = pd.read_sql_query('select cost, price, name, product_id from products', conn)
pruducts_ids_names = [f"{product_id} - {name}" for name, product_id in zip(pruducts['name'], pruducts['product_id'])]
#products_costs_prices = 

# DB Close
conn.close()

# DATA INSERT

with st.sidebar:
    st.title('Sidebar')
    st.text('Sidebar')

tab1, tab2, tab3 = st.tabs(['Dashboard','Raw Data','Management'])

with tab2:
    st.dataframe(clients_names)

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
            product = st.selectbox('Products', pruducts_ids_names)
            if product:
                product_id = product.split(' - ')[0]
            ## sold_products = st.
            quantity_sold = st.number_input('Amount', value=None)
            # unit_price = st.
            # total_price = st.
            discounts = st.number_input('Discounts')
            additional_fees = st.number_input('Additional Fees')
            payment_method = st.selectbox('Payment Method', ['Cash', 'Card', 'Other'])
            transaction_status = st.selectbox('Status', ['Done','Waiting for Payment'])
            delivery_method = st.selectbox('Delivery Method', ['Store', 'Delivery'])
            employee_id = st.selectbox('Seller', ['1 - Mary','2 - Joseph','3 - Paul'])
            sale_location = st.selectbox('Storage',['Malibu', 'Silicon Valley', 'Central'])
            # coupon_code_used = st.
            # additional_notes = st.
            sendSale = st.form_submit_button("Register")
        if sendSale:
            #defs.insertSaleDB(product_name=name, product_category=category)
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

            
    