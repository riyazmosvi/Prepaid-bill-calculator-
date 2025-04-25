import streamlit as st
from datetime import datetime
import math

# Title
st.set_page_config(page_title="Prepaid Bill Calculator", layout="centered")
st.title("Prepaid Bill Calculator 💡")

# Input fields
rate_code = st.selectbox("Select Rate Code", [
    "Rate Code 1",
    "Rate Code 2: Phase 1",
    "Rate Code 2: Phase 3"
])

start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

demand = st.number_input("Demand (kW)", min_value=0.0, format="%.2f")
total_units = st.number_input("Total Units Consumed", min_value=0.0, format="%.2f")

# Helper functions
def calculate_rate_code_1(units_per_month, demand, months):
    total_amount = 0
    for _ in range(months):
        if units_per_month <= 200:
            amount = units_per_month * 2.30
        elif units_per_month <= 400:
            amount = 200 * 2.30 + (units_per_month - 200) * 4.00
        else:
            amount = 200 * 2.30 + 200 * 4.00 + (units_per_month - 400) * 4.35
        discount = -0.02 * amount
        demand_charges = 8 * demand
        total_amount += amount + discount + demand_charges
    return total_amount

def calculate_rate_code_2_phase_1(units_per_month, demand, months):
    total_amount = 0
    for _ in range(months):
        if units_per_month <= 200:
            amount = units_per_month * 3.55
        elif units_per_month <= 500:
            amount = 200 * 3.55 + (units_per_month - 200) * 5.40
        else:
            amount = 200 * 3.55 + 300 * 5.40 + (units_per_month - 500) * 5.85
        discount = -0.02 * amount
        demand_charges = 60 * demand
        total_amount += amount + discount + demand_charges
    return total_amount

def calculate_rate_code_2_phase_3(units_per_month, demand, months):
    total_amount = 0
    for _ in range(months):
        amount = units_per_month * 5.85
        discount = -0.02 * amount
        demand_charges = (demand / 0.9) * 130
        total_amount += amount + discount + demand_charges
    return total_amount

# Form submission
if st.button("Calculate Bill"):
    try:
        if start_date > end_date:
            st.error("Start date must be before end date.")
        elif demand <= 0 or total_units <= 0:
            st.error("Please enter valid values for demand and total units.")
        else:
            months = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month + 1
            units_per_month = math.ceil(total_units / months)

            if rate_code == "Rate Code 1":
                result = calculate_rate_code_1(units_per_month, demand, months)
            elif rate_code == "Rate Code 2: Phase 1":
                result = calculate_rate_code_2_phase_1(units_per_month, demand, months)
            elif rate_code == "Rate Code 2: Phase 3":
                result = calculate_rate_code_2_phase_3(units_per_month, demand, months)

            st.success(f"Total Bill Amount: ₹{result:.2f}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Inspirational Quotes
st.markdown("---")
quotes = [
    "💡 Automation makes life easier!",
    "📈 Work smarter, not harder.",
    "📚 Knowledge enlivens the soul.",
    "🔍 Wisdom is the lost property of the believer.",
    "💎 The noblest wealth is the wealth of knowledge."
]
from random import choice
st.info(choice(quotes))

# Footer
st.markdown("#### 👨‍💻 Developed by: ER-SYED RIYAZ")
