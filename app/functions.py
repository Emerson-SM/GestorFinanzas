import streamlit as st
import pandas as pd
import json
import os
from app.tables import create_tables
from app.styles import apply_custom_styles

file_json = 'categories.json'
  
if 'categories' not in st.session_state:
    st.session_state.categories = {
        'Uncategorized': []
    }
    if os.path.exists(file_json):
        with open(file_json, 'r') as f:
            st.session_state.categories = json.load(f)

def save_categories():
    with open(file_json, 'w') as f:
        json.dump(st.session_state.categories, f)

def categorize_transactions(df):
    df['Category'] = 'Uncategorized'

    for category, keywords in st.session_state.categories.items():
        if category == 'Uncategorized' or not keywords:
            continue

        lowered_keywords = [str(keyword).lower().strip() for keyword in keywords]

        for idx, row in df.iterrows():
            details = row['Details'].lower().strip()
            if details in lowered_keywords:
                df.at[idx, 'Category'] = category

    return df

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

        return categorize_transactions(df)
    except Exception as e:
        st.error(f'Error processing file: {str(e)}')
        return None

def add_keyword_category(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False

def main_function():

    apply_custom_styles()

    save_categories()

    st.title('Personal Finance Analytics Dashboard')

    upload_file = st.file_uploader('Put here your CSV or Excel file', type=['csv', 'xlsx', 'xls'])

    if upload_file is not None: 

        df = load_transactions(upload_file)

        if df is not None:

            debits = df[df["Debit/Credit"] == "Debit"].copy()
            credits = df[df["Debit/Credit"] == "Credit"].copy()
                        
            st.session_state.debits = debits.copy()
            st.session_state.credits = credits.copy()

            table1, table2 = st.tabs(
                ['Expensives (Debits)', 'Payments (Credits)']
            )

            create_tables(table1, table2)      