import streamlit as st
from database import set_budget, get_all_budgets

def render_settings():
    st.title("⚙️ Settings")
    
    st.subheader("Set Monthly Budgets")
    st.write("Set budget limits for your frequent categories to track spending.")
    
    current_budgets = get_all_budgets()
    
    categories = [
        "Food", "Transport", "Utilities", "Groceries", 
        "Entertainment", "Health", "Shopping", "Personal", "Other"
    ]
    
    with st.form("budget_form"):
        for cat in categories:
            val = current_budgets.get(cat, 0.0)
            amount = st.number_input(f"{cat} Budget", min_value=0.0, value=val, step=10.0, format="%.2f")
            
            # Use session state to capture values temporarily
            st.session_state[f"budget_{cat}"] = amount
            
        submitted = st.form_submit_button("Save Budgets")
        if submitted:
            for cat in categories:
                set_budget(cat, st.session_state[f"budget_{cat}"])
            st.success("Budgets updated successfully!")
            
    st.divider()
    st.subheader("Data Management")
    st.warning("Advanced options")
    if st.button("Clear All Data"):
        st.error("This feature is disabled for safety in this version.")
