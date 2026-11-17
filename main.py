import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
import json
import os

st.set_page_config(page_title="Finance Manage", page_icon="🪙", layout="wide")

def load_transactions(file):

    file_name = file.name.lower()
    try:
        if file_name.endswith(('.csv')):
            df = pd.read_csv(file)
        elif file_name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file)

        df.columns = [col.strip() for col in df.columns]
        df['Amount'] = df['Amount'].str.replace(',', '').astype(float)
        df['Date'] = pd.to_datetime(df['Date'], format='%d %b %Y')

        st.write(df)

        return df
    except Exception as e:
        st.error(f'Error processing file: {str(e)}')
        return None



def main_function():
    st.title("Dashboard For Manage Finances")

    upload_file = st.file_uploader("Put here your CSV or Excel file", type=["csv", "excel"])

    if upload_file is not None: 

        df = load_transactions(upload_file)

main_function()