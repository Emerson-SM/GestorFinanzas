import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
from app.functions import save_categories, add_keyword_category

def create_tables(t1, t2):
    with t1:
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
                    new_category = row['Category']
                    if new_category == st.session_state.debits.at[idx, 'Category']:
                        continue
                        
                    details = row['Details']
                    st.session_state.debits.at[idx, 'Category'] = new_category
                    add_keyword_category(new_category, details)
                        
            st.subheader('Expense Summary')
            category_totals = st.session_state.debits.groupby('Category')['Amount'].sum().reset_index()
            category_totals = category_totals.sort_values('Amount', ascending=False)
                
            st.dataframe(
                category_totals, 
                column_config={
                    'Amount': st.column_config.NumberColumn('Amount', format='%.2f AED')   
                },
                use_container_width=True,
                hide_index=True
            )
                
            fig = px.pie(
                category_totals,
                values='Amount',
                names='Category',
                title='Expenses by Category'
            )
            st.plotly_chart(fig, use_container_width=True)
                
    with t2:
        st.subheader('Payments Summary')
        total_payments = credits['Amount'].sum()
        st.metric('Total Payments', f'{total_payments:,.2f} AED')
        st.write(credits)   