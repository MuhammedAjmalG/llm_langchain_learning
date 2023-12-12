import streamlit as st
from helper import get_restaurant_name_menu

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Select a cuisine",("Indian", "Italian", "Mexican", "Arabic", "American"))
if cuisine:
    response = get_restaurant_name_menu(cuisine=cuisine)
    st.header(response['cuisine_name'].strip())
    menu_items = response['menu_list'].strip().split(",")
    st.title("Menu list")
    for item in menu_items:
        st.write("-",item)
