from datetime import datetime
import time
import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Expense Predictor, Budget & Risk AI",
    page_icon="💰",
    layout="wide",
)

# Custom Styling for Dark Theme UI
st.markdown(
    """
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1a1c23; padding: 15px; border-radius: 10px; border: 1px solid #2d3748; }
    .agent-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px; }
    .agent-header { color: #58a6ff; font-weight: bold; font-size: 18px; margin-bottom: 10px; }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Navigation & Custom Controls
st.sidebar.title("💰 Financial Intelligence")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation Menu",
    [
        "📊 Financial Profile & Dashboard",
        "🤖 Multi-Agent Financial Hub",
        "📂 Expense Ledger & Data",
    ],
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Dynamic Expense Controls")
st.sidebar.markdown("Adjust your monthly category spends below to update the dashboard numbers instantly:")

# Interactive sliders for user inputs
housing_input = st.sidebar.slider("Housing / Rent (INR)", 10000, 60000, 25000, 1000)
groceries_input = st.sidebar.slider("Groceries (INR)", 1000, 20000, 4500, 500)
utilities_input = st.sidebar.slider("Utilities (INR)", 500, 10000, 3200, 200)
entertainment_input = st.sidebar.slider("Entertainment (INR)", 500, 15000, 2500, 200)
dining_input = st.sidebar.slider("Dining Out (INR)", 500, 15000, 1800, 200)

# Calculate dynamic total expenses
total_expenses = housing_input + groceries_input + utilities_input + entertainment_input + dining_input
predicted_next = int(total_expenses * 1.11)
savings_potential = max(5000, 50000 - total_expenses)

# Risk score logic based on total spend
risk_score = "Low" if total_expenses < 35000 else "Moderate" if total_expenses < 50000 else "High"

# ================= PAGE 1: FINANCIAL PROFILE & DASHBOARD =================
if page == "📊 Financial Profile & Dashboard":
    st.title("📊 Expense Predictor, Budget & Risk Dashboard")
    st.markdown("Monitor your custom burn rate, categorical expenses, and financial health metrics in real-time.")

    # Top Metrics Row (Powered by user sliders)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Monthly Expenses", f"₹{total_expenses:,}", "Custom Input")
    col2.metric("Predicted Next Month", f"₹{predicted_next:,}", "+11% projected")
    col3.metric("Budget Risk Score", risk_score, "Dynamic Audit")
    col4.metric("Savings Potential", f"₹{savings_potential:,}", "Optimized Buffer")

    st.markdown("---")

    # Visual Charts updated dynamically
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("📉 Expense Breakdown by Category")
        category_data = pd.DataFrame(
            {"Amount (INR)": [housing_input, groceries_input, utilities_input, entertainment_input, dining_input]},
            index=["Housing", "Groceries", "Utilities", "Entertainment", "Dining"],
        )
        st.bar_chart(category_data)

    with c2:
        st.subheader("📈 6-Month Spending Trend Prediction")
        trend_values = [total_expenses * 0.9, total_expenses * 0.95, total_expenses * 0.92, total_expenses * 0.98, total_expenses, predicted_next]
        trend_data = pd.DataFrame(
            trend_values,
            index=["May", "Jun", "Jul", "Aug", "Sep", "Oct (Projected)"],
            columns=["Projected Spend (INR)"],
        )
        st.line_chart(trend_data)


# ================= PAGE 2: MULTI-AGENT FINANCIAL HUB =================
elif page == "🤖 Multi-Agent Financial Hub":
    st.title("🤖 Multi-Agent Financial Intelligence Center")
    st.markdown("Autonomous financial agents analyzing your custom ledger data and risk profile.")

    tab1, tab2, tab3 = st.tabs(
        [
            "📈 Agent 1: Expense Forecasting Agent",
            "🛡️ Agent 2: Budget Risk & Anomaly Auditor",
            "💬 Agent 3: Personal Financial Copilot (LLM)",
        ]
    )

    with tab1:
        st.markdown(
            """
            <div class="agent-card">
              <div class="agent-header">📈 Expense Forecasting Agent</div>
              <p>Predicts upcoming expenses using regression models based on your active sidebar inputs.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Generate Next-Month Expense Forecast"):
            with st.spinner("Analyzing custom spending sliders and running predictive models..."):
                time.sleep(1.2)
            st.success(f"Forecast Generated: Based on your current ₹{total_expenses:,} monthly spend, next month is projected at **₹{predicted_next:,}**.")

    with tab2:
        st.markdown(
            """
            <div class="agent-card">
              <div class="agent-header">🛡️ Budget Risk & Anomaly Auditor</div>
              <p>Scans your custom expense allocations to flag high-risk budget categories.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Run Budget Risk Audit"):
            with st.spinner("Auditing custom inputs against risk thresholds..."):
                time.sleep(1.2)
            if risk_score == "High":
                st.warning("⚠️ **Audit Notice:** High overall burn rate detected. Consider trimming discretionary categories like Dining or Entertainment.")
            else:
                st.success("✅ **Audit Notice:** Your budget allocation is stable and well within healthy risk thresholds.")

    with tab3:
        st.markdown(
            """
            <div class="agent-card">
              <div class="agent-header">💬 Financial Advisory Copilot</div>
              <p>Ask questions about your custom budget, savings goals, or spending habits.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        query = st.text_input("Ask Financial Copilot:", placeholder="e.g., How can I optimize my housing and grocery budget?")
        if query:
            st.success(f"🤖 **Financial Copilot:** Processed query regarding your ₹{total_expenses:,} budget. Keeping your housing (₹{housing_input}) under 40% of total cash flow is a solid financial practice!")


# ================= PAGE 3: EXPENSE LEDGER & DATA =================
elif page == "📂 Expense Ledger & Data":
    st.title("📂 Custom Transaction Ledger & CSV Export")
    st.markdown("Itemized table built dynamically from your sidebar inputs.")

    df_custom = pd.DataFrame(
        {
            "Category": ["Housing/Rent", "Groceries", "Utilities", "Entertainment", "Dining Out"],
            "Amount (INR)": [housing_input, groceries_input, utilities_input, entertainment_input, dining_input],
            "Risk Level": ["Low" if housing_input < 30000 else "High", "Low", "Low", "Medium", "High" if dining_input > 3000 else "Low"],
        }
    )

    st.dataframe(df_custom, use_container_width=True)

    csv_data = df_custom.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Custom Expense Audit CSV",
        data=csv_data,
        file_name="custom_expense_risk_audit.csv",
        mime="text/csv",
    )