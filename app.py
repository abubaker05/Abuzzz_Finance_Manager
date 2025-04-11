import streamlit as st
import pandas as pd
from utils.fraud_detector import detect_fraud
from utils.balance_sheet import calculate_balance
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random

st.set_page_config(page_title="Abuzzz Finance Manager", layout="wide")

st.title("📁 Abuzzz Finance Manager — Fraud Detection App")

uploaded_file = st.file_uploader("👉 Upload your CSV file", type=["csv"])

# Initialize df_fraud and fraud_only to avoid reference error
df_fraud = None
fraud_only = None

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    # st.write("👉 Columns:", df.columns.tolist())

    if st.button("📄 View Data"):
        st.subheader("Uploaded Data")
        st.dataframe(df)

    if st.button("🧠 Detect Fraud"):
        df_fraud = detect_fraud(df)
        fraud_only = df_fraud[df_fraud["is_fraud"] == 1]
        st.session_state['df_fraud'] = df_fraud

        st.subheader("🚨 Fraudulent Transactions Detected")

        if fraud_only.empty:
            st.success("No fraudulent transactions found! ✅")
        else:
            st.dataframe(fraud_only)

    if st.button("📊 View Balance Sheet"):
        income, expense, net = calculate_balance(df)
        st.metric("Total Income", f"₹ {income}")
        st.metric("Total Expense", f"₹ {expense}")
        st.metric("Net Balance", f"₹ {net}")

    if st.button("📈 Visualize"):
        st.subheader("Amount by Type")
        plt.figure(figsize=(8, 4))
        sns.barplot(x="type", y="amount", data=df)
        st.pyplot(plt)

    if st.button("💡 Suggest Me Something"):
        tips = [
            "Always double-check unknown transactions.",
            "Avoid sharing OTPs with anyone.",
            "Track expenses weekly to spot issues early.",
            "Set daily limits on UPI/wallet transactions.",
            "Use strong passwords on banking apps."
        ]
        st.info("💡 Tip: " + random.choice(tips))

    if st.button("📤 Export PDF Report"):
        st.warning("🚧 PDF export coming soon!")

else:
    st.info("⬆️ Upload a CSV file to get started.")
