import streamlit as st
from utils.file_handler import process_csv_upload
from database import add_transaction

def render_upload_data():
    st.title("📂 Upload Data")
    st.write("Upload your bank or MoMo statements in CSV format.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            df = process_csv_upload(uploaded_file)
            st.write("### Preview:")
            st.dataframe(df)
            
            if st.button("Confirm & Import", type="primary"):
                count = 0
                for _, row in df.iterrows():
                    add_transaction(
                        date=row['date'],
                        amount=row['amount'],
                        category=row['category'],
                        description=row['description'],
                        payment_method=row['payment_method'],
                        subcategory=row['subcategory'],
                        tags=row['tags']
                    )
                    count += 1
                st.success(f"Successfully imported {count} transactions!")
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
