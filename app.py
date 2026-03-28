import streamlit as st
import os
from database import init_db

# Component imports
from components.dashboard import render_dashboard
from components.add_expense import render_add_expense
from components.upload_data import render_upload_data
from components.reports import render_reports
from components.settings import render_settings

# Configure the Streamlit page
st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_db()

def main():
    st.sidebar.title("💰 Expense Tracker")
    st.sidebar.write("Track smartly, spend wisely.")
    st.sidebar.divider()
    
    # Sidebar navigation
    page = st.sidebar.radio("Navigation", [
        "Dashboard", 
        "Add Expense", 
        "Upload Data", 
        "Reports", 
        "Settings"
    ])
    
    # Route to the appropriate page component
    if page == "Dashboard":
        render_dashboard()
    elif page == "Add Expense":
        render_add_expense()
    elif page == "Upload Data":
        render_upload_data()
    elif page == "Reports":
        render_reports()
    elif page == "Settings":
        render_settings()
        
    st.sidebar.divider()
    st.sidebar.info("v1.0 | Low Friction Tracking")

if __name__ == "__main__":
    main()
