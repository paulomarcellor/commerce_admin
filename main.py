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
    col31, col32, col33 = st.columns(3)
    with col31:
        insertSale = st.button('Insert Sale', key='btnSale')
    with col32:
        insertClient = st.button('Insert Client', key='btnClient')
    with col33:
        insertProduct = st.button('Insert Product', key='btnProduct')
    if insertProduct:
        with st.form("my_form"):
            name = st.text_input("Name")
            category = st.text_input("Category")
            submit_button = st.form_submit_button("Send")
            if submit_button:
                st.success('Success!')
                defs.insertProductDB(name, category)
                st.success('Success!')

            
    