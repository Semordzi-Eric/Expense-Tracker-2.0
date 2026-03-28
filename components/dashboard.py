import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from database import get_all_transactions, get_all_budgets

def render_dashboard():
    st.title("📊 Dashboard")
    
    df = get_all_transactions()
    budgets = get_all_budgets()
    
    if df.empty:
        st.info("No transactions found. Start by adding an expense or uploading a CSV!")
        return
        
    df['date'] = pd.to_datetime(df['date'])
    current_month = datetime.now().strftime('%Y-%m')
    df_month = df[df['date'].dt.strftime('%Y-%m') == current_month]
    
    total_spent_month = df_month['amount'].sum()
    total_spent_all = df['amount'].sum()
    
    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Spent (This Month)", f"GH₵ {total_spent_month:,.2f}")
    col2.metric("Total Spent (All Time)", f"GH₵ {total_spent_all:,.2f}")
    
    # Budgets
    if budgets:
        total_budget = sum(budgets.values())
        budget_remaining = total_budget - total_spent_month
        col3.metric("Budget Remaining", f"GH₵ {budget_remaining:,.2f}")
    else:
        col3.metric("Budget Remaining", "Not Set")
    
    st.divider()
    
    # Visualizations
    col_chart1, col_chart2 = st.columns(2)
    
    # Spending by category
    category_spend = df_month.groupby('category')['amount'].sum().reset_index()
    if not category_spend.empty:
        fig_pie = px.pie(category_spend, values='amount', names='category', title='Spending by Category (This Month)', hole=0.4)
        col_chart1.plotly_chart(fig_pie, use_container_width=True)
        
    # Daily spending trend
    daily_spend = df_month.groupby(df_month['date'].dt.date)['amount'].sum().reset_index()
    if not daily_spend.empty:
        fig_line = px.line(daily_spend, x='date', y='amount', title='Daily Spending Trend (This Month)', markers=True)
        col_chart2.plotly_chart(fig_line, use_container_width=True)
        
    st.divider()
    
    # Insights
    st.subheader("💡 Financial Insights")
    insights = []
    
    if not category_spend.empty:
        top_category = category_spend.loc[category_spend['amount'].idxmax()]
        pct = (top_category['amount'] / total_spent_month) * 100
        insights.append(f"You spend **{pct:.1f}%** of your money on **{top_category['category']}**.")
        
    # Budget alerts
    for cat, limit in budgets.items():
        cat_spent = df_month[df_month['category'] == cat]['amount'].sum()
        if cat_spent > limit:
            insights.append(f"🚨 **Alert**: You have exceeded your {cat} budget by GH₵ {(cat_spent - limit):.2f}!")
        elif cat_spent > limit * 0.8:
            insights.append(f"⚠️ **Warning**: You are nearing your {cat} budget ({cat_spent:.2f} / {limit:.2f}).")
            
    if insights:
        for insight in insights:
            st.markdown(f"- {insight}")
    else:
        st.write("No critical insights to show right now. Keep logging expenses!")
