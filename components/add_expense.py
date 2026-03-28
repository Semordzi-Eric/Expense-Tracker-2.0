import streamlit as st
from utils.parser import parse_bulk_quick_add
from database import add_transaction

def render_add_expense():
    st.title("➕ Add Expense")
    
    st.subheader("🚀 Quick Add")
    quick_input = st.text_area("Enter expenses (e.g., 'Friday\\nFood 20, 10\\nWater 5')", key="quick_add_input", height=150)
    
    if st.button("Add Fast", type="primary"):
        if quick_input:
            try:
                transactions = parse_bulk_quick_add(quick_input)
                if not transactions:
                    st.warning("Could not parse any amounts. Check your format.")
                else:
                    for data in transactions:
                        add_transaction(**data)
                    st.success(f"Successfully added {len(transactions)} expenses!")
                    for t in transactions:
                        st.write(f"- GH₵ {t['amount']} for {t['category']} ({t['description']}) on {t['date'][:10]}")
            except Exception as e:
                st.error(f"Error parsing input: {str(e)}")
        else:
            st.warning("Please enter an expense.")
            
    st.divider()
    
    st.subheader("📝 Manual Entry")
    with st.form("manual_expense_form"):
        col1, col2 = st.columns(2)
        amount = col1.number_input("Amount", min_value=0.01, format="%.2f")
        date_val = col2.date_input("Date")
        
        col3, col4 = st.columns(2)
        category = col3.selectbox("Category", [
            "Food", "Transport", "Utilities", "Groceries", 
            "Entertainment", "Health", "Shopping", "Personal", "Transfer", "Other"
        ])
        payment_method = col4.selectbox("Payment Method", ["Cash", "Mobile Money", "Bank Transfer", "Credit Card"])
        
        description = st.text_input("Description (Optional)")
        
        submitted = st.form_submit_button("Save Expense")
        if submitted:
            add_transaction(
                date=date_val.strftime("%Y-%m-%d %H:%M:%S"),
                amount=amount,
                category=category,
                description=description,
                payment_method=payment_method
            )
            st.success("Expense saved successfully!")
