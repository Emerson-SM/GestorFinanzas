import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
import json
import os

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

    lowered_keywords = [keywords.lower().strip() for keyword in keywords]

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
    st.title("Dashboard For Manage Finances")

    upload_file = st.file_uploader("Put here your CSV or Excel file", type=["csv", "excel"])

    if upload_file is not None: 

        df = load_transactions(upload_file)

        if df is not None:
            debits = df[df['Debit/Credit'] == 'Debit'].copy()
            credits = df[df['Debit/Credit'] == 'Credit'].copy()

            st.session_state.debits = debits.copy()

            table1, table2 = st.tabs(['Expensives (Debits)', 'Payments (Credits)'])

            with table1:
                new_category = st.text_input('Write a new category: ')
                add_button = st.button('Add this category')

                if add_button and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.rerun()

                st.subheader('Your Expenses')
                edited_df = st.data_editor(
                    st.session_state.debits[['Date', 'Details', 'Amount', 'Category']],
                    column_config={
                        'Date': st.column_config.DateColumn('Date', format='DD/MM/YYYY'),
                        'Amount': st.column_config.NumberColumn('Amount', format='%.2f AED'),
                        'Category': st.column_config.SelectboxColumn(
                        'Category',
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key='category_editor'
                )
                save_button = st.button('Apply Changes', type='primary')
                if save_button:
                    for idx, row in edited_df.iterrows():
                        new_category = row["Category"]
                        if new_category == st.session_state.debits.at[idx, "Category"]:
                            continue
                        
                        details = row["Details"]
                        st.session_state.debits_df.at[idx, "Category"] = new_category
                        add_keyword_category(new_category, details)
                        
                st.subheader('Expense Summary')
                category_totals = st.session_state.debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_totals = category_totals.sort_values("Amount", ascending=False)
                
                st.dataframe(
                    category_totals, 
                    column_config={
                     "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED")   
                    },
                    use_container_width=True,
                    hide_index=True
                )
                
                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)
                
            with table2:
                st.subheader("Payments Summary")
                total_payments = credits["Amount"].sum()
                st.metric("Total Payments", f"{total_payments:,.2f} AED")
                st.write(credits)