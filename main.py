import streamlit as st
from app.functions import main_function

st.set_page_config(page_title='Personal Finances', page_icon='🪙', layout='wide')

main_function()