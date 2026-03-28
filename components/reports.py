import streamlit as st
import pandas as pd
from database import get_all_transactions

def render_reports():
    st.title("📄 Reports & Analytics")
    
    df = get_all_transactions()
    
    if df.empty:
        st.info("No transactions available for reporting.")
        return
        
    df['date'] = pd.to_datetime(df['date'])
    
    st.subheader("Filter Transactions")
    col1, col2, col3 = st.columns(3)
    
    # Date range
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    
    date_range = col1.date_input("Date Range", [min_date, max_date])
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        mask = (df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)
        filtered_df = df.loc[mask]
    else:
        filtered_df = df
        
    # Category filter
    categories = ["All"] + list(df['category'].unique())
    selected_category = col2.selectbox("Category", categories)
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df['category'] == selected_category]
        
    # Payment Method filter
    methods = ["All"] + list(df['payment_method'].unique())
    selected_method = col3.selectbox("Payment Method", methods)
    if selected_method != "All":
        filtered_df = filtered_df[filtered_df['payment_method'] == selected_method]
        
    st.divider()
    
    st.subheader("Filtered Results")
    st.metric("Total Result Amount", f"GH₵ {filtered_df['amount'].sum():,.2f}")
    
    # Display table
    st.dataframe(filtered_df, use_container_width=True)
    
    # Export options
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Report as CSV",
        data=csv,
        file_name='expense_report.csv',
        mime='text/csv',
    )
