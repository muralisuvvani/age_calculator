import streamlit as st
from datetime import date
import base64

# ✅ Set page config
st.set_page_config(page_title="Antique Age Engine", page_icon="⌛", layout="centered")

# ✅ Set background
def set_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            font-family: 'Georgia', serif;
        }}
        .main-title {{
            color: #3e2f1c;
            background-color: rgba(255, 248, 220, 0.7);
            text-align: center;
            font-size: 45px;
            font-weight: bold;
            padding: 15px 25px;
            border: 3px double #3e2f1c;
            border-radius: 10px;
            margin-bottom: 30px;
            text-shadow: 1px 1px #d6b978;
        }}
        label, .stNumberInput label, .stTextInput label {{
            color: #4e3d2c !important;
            font-weight: bold;
            font-size: 18px;
            background-color: rgba(255, 255, 240, 0.6);
            padding: 5px 8px;
            border-radius: 8px;
        }}
        .stButton>button {{
            background-color: #8b5e3c;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
            border: none;
        }}
        .stButton>button:hover {{
            background-color: #a76b47;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Apply background
set_bg_from_local("background_cal.jpeg")

# ✅ Title
st.markdown("<div class='main-title'>🕰️ The Grand Age Engine</div>", unsafe_allow_html=True)
st.markdown("Enter your details to calculate your age:")

# ✅ Input form (no pre-filled default values)
with st.form("age_form"):
    name = st.text_input("📜 Your Given Name:")
    year = st.number_input("📅 Year of Birth:", min_value=1800, max_value=date.today().year, step=1)
    month = st.number_input("🌙 Birth Month:", min_value=1, max_value=12, step=1)
    day = st.number_input("☀️ Birth Day:", min_value=1, max_value=31, step=1)
    submit = st.form_submit_button("🔍 Reveal My Age")

# ✅ Process on submit
if submit:
    try:
        birthdate = date(int(year), int(month), int(day))
        today = date.today()

        # Age calculation
        years = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            years -= 1

        months = today.month - birthdate.month
        if today.day < birthdate.day:
            months -= 1
        if months < 0:
            months += 12

        if today.day >= birthdate.day:
            days = today.day - birthdate.day
        else:
            prev_month = today.month - 1 or 12
            prev_year = today.year if today.month != 1 else today.year - 1
            days_in_prev_month = (date(today.year, today.month, 1) - date(prev_year, prev_month, 1)).days
            days = days_in_prev_month + today.day - birthdate.day

        total_days = (today - birthdate).days

        st.markdown(
            f"""
            <div style="
                background-color: rgba(255, 255, 240, 0.9);
                color: #3e2f1c;
                border: 2px solid #8b5e3c;
                padding: 20px;
                border-radius: 12px;
                font-size: 18px;
                box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 15px;
            ">
                🧭 <strong>{name}</strong>, your journey spans <strong>{years} years, {months} months, and {days} days</strong>.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                background-color: rgba(245, 235, 200, 0.85);
                color: #3e2f1c;
                border: 2px dashed #a67c52;
                padding: 18px;
                border-radius: 12px;
                font-size: 17px;
                box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.05);
            ">
                ⏳ You’ve walked the earth for <strong>{total_days:,} days</strong> in time.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    except Exception:
        st.error("⚠️ Invalid date. Please check the values.")
