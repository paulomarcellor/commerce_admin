import streamlit as st
import sqlite3 as sql
import pandas as pd
import defs

st.set_page_config(page_title="Commerce Admin", layout="wide", initial_sidebar_state="auto")
st.title('Commerce Administration')

# DATA INSERT

with st.sidebar:
    st.title('Sidebar')
    st.text('Sidebar')
    

tab1, tab2, tab3 = st.tabs(['Dashboard','Raw Data','Management'])

# MANAGEMENT
with tab3:
    st.header('Management System')
    col31, col32, col33 = st.columns(3)
    with col31:
        # Sales Form
        with st.form("Register Sale", clear_on_submit=True):
            st.header('Register Sale')
            name = st.text_input("Name")
            category = st.text_input("Category")
            sendSale = st.form_submit_button("Register")
        if sendSale:
            #defs.insertProductDB(product_name=name, product_category=category)
            st.success('Success!')
    with col32:
        # Clients Form
        with st.form("Register Client", clear_on_submit=False):
            st.header('Register Client')
            client_name=st.text_input('Name')
            client_age=st.number_input('Age')
            client_sex=st.selectbox('Sex', ['Male','Female'])
            client_marital_status=st.selectbox('Marital Status', ['Single','Married', 'Divorced', 'Widowed'])
            client_email=st.text_input('E-mail')
            client_phone=st.text_input('Phone Number')
            client_occupation=st.text_input('Occupation')
            client_preferencial_communication=st.selectbox('Preferencial Communication', ['Phone', 'SMS', 'E-mail'])
            client_location=st.text_input('Location')
            sendClient = st.form_submit_button('Register')
        if sendClient:
            defs.insertClientDB(client_name, client_age, client_sex, client_marital_status,\
                   client_email, client_phone, client_occupation, client_preferencial_communication,\
                    client_location)
            st.success(str(client_name) + ' Registered Successfully')
        
    with col33:
        # Products Form
        with st.form("Register Product", clear_on_submit=True):
            st.header('Register Product')
            name = st.text_input("Name")
            category = st.text_input("Category")
            sendProduct = st.form_submit_button("Register")
        if sendProduct:
            defs.insertProductDB(product_name=name, product_category=category)
            st.success('Success!')

            
    