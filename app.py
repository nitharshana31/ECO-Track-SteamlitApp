# app.py – EcoTrack Carbon Footprint Application (Final + Extra Animations)

import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="EcoTrack – Carbon Footprint",
    page_icon="🌿",
    layout="wide"
)

# ---------------------------------------------------------
# PREMIUM ECO CSS – HIGH VISIBILITY FIX
# ---------------------------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #F1F8E9, #E8F5E9, #C8E6C9);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

[data-testid="stSidebar"] {
    background: #1B5E20;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
    font-weight: 500;
}

h1 {
    font-size: 48px !important;
    font-weight: 800 !important;
    color: #1B5E20 !important;
    text-align: center;
}

.eco-card {
    background: rgba(255,255,255,0.92);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 15px 35px rgba(46,125,50,0.25);
    border-left: 6px solid #2E7D32;
    margin-bottom: 20px;
}

.section-energy {
    background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
    border-radius: 18px;
    padding: 20px;
}
.section-travel {
    background: linear-gradient(135deg, #FFF8E1, #FFE0B2);
    border-radius: 18px;
    padding: 20px;
}
.section-result {
    background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
    border-radius: 18px;
    padding: 20px;
}

.stButton>button {
    background: linear-gradient(90deg, #43A047, #1B5E20);
    color: white !important;
    border-radius: 16px;
    padding: 12px 28px;
    font-size: 18px;
    font-weight: 700;
}

.progress {
    height: 14px;
    background: #C8E6C9;
    border-radius: 10px;
}
.progress > .fill {
    height: 100%;
    background: linear-gradient(90deg, #66BB6A, #2E7D32);
    border-radius: 10px;
}

.sidebar-box {
    background: rgba(255,255,255,0.15);
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 14px;
            

}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SAFE LOTTIE LOADER
# ---------------------------------------------------------
def load_lottie(url):
    try:
        r = requests.get(url, timeout=4)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return None

# ---------------------------------------------------------
# LOTTIE ANIMATIONS
# ---------------------------------------------------------
lottie_leaf = load_lottie("https://assets6.lottiefiles.com/packages/lf20_kyu7xb1v.json")
lottie_earth = load_lottie("https://assets7.lottiefiles.com/packages/lf20_xvrofzfk.json")
lottie_energy = load_lottie("https://assets5.lottiefiles.com/packages/lf20_jtbfg2nb.json")
lottie_travel = load_lottie("https://assets2.lottiefiles.com/packages/lf20_ydo1amjm.json")
lottie_calc = load_lottie("https://assets2.lottiefiles.com/packages/lf20_x62chJ.json")
lottie_success = load_lottie("https://assets8.lottiefiles.com/packages/lf20_qmfs6c3i.json")
lottie_footer = load_lottie("https://assets4.lottiefiles.com/packages/lf20_gjmecwii.json")
lottie_insight = load_lottie("https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json")
lottie_growth = load_lottie("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")
lottie_sustain = load_lottie("https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json")

# ---------------------------------------------------------
# EMISSION FACTORS
# ---------------------------------------------------------
EMISSION_FACTORS = {
    "electricity_kwh": 0.82,
    "lpg_kg": 2.98,
    "waste_kg": 0.45,
    "water_litre": 0.0003,
    "public_transport_km": 0.105,
    "car_km": 0.180,
    "bike_km": 0.065,
    "air_km": 0.255,
}

# ---------------------------------------------------------
# CARBON CALCULATION
# ---------------------------------------------------------
def calculate_carbon(e, lpg, car, bike, public, air, waste, water):
    values = {
        "Electricity ⚡": e * EMISSION_FACTORS["electricity_kwh"],
        "LPG 🔥": lpg * EMISSION_FACTORS["lpg_kg"],
        "Car 🚗": car * 30 * EMISSION_FACTORS["car_km"],
        "Bike 🚲": bike * 30 * EMISSION_FACTORS["bike_km"],
        "Public Transport 🚌": public * 30 * EMISSION_FACTORS["public_transport_km"],
        "Air ✈️": air * EMISSION_FACTORS["air_km"],
        "Waste 🗑": waste * 4 * EMISSION_FACTORS["waste_kg"],
        "Water 💧": water * 30 * EMISSION_FACTORS["water_litre"],
    }
    return sum(values.values()), values

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## 🌿 EcoTrack")

    if lottie_leaf:
        st_lottie(lottie_leaf, height=110)

    menu = st.radio("Navigation", ["🏠 Home", "🧮 Calculator", "ℹ️ About"])

    st.markdown("🌍 **Eco Tip:** Reduce car usage to lower emissions")

    if lottie_footer:
        st_lottie(lottie_footer, height=90)

    st.markdown("---")

    st.markdown("""
    <div class="sidebar-box">
        <h4>📊 Impact Summary</h4>
        <p style="font-size:13px;">
        Track how small daily actions contribute to a greener planet.
        </p>
    </div>
    """, unsafe_allow_html=True)

    colA, colB = st.columns(2)
    with colA:
        st.metric("🌱 Goal", "Low Carbon")
    with colB:
        st.metric("🌍 Status", "Tracking")

    if lottie_insight:
        st_lottie(lottie_insight, height=100)

# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------
if menu == "🏠 Home":
    st.markdown("<h1>EcoTrack – Carbon Footprint Tracker</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if lottie_earth:
            st_lottie(lottie_earth, height=320)
        if lottie_growth:
            st_lottie(lottie_growth, height=160)
    with col2:
        st.markdown("""
        <div class="eco-card">
        <h3>Track • Understand • Reduce</h3>
        <p style="font-size:18px">
        EcoTrack enables users to understand their environmental impact through
        intuitive inputs, real-time calculations, and interactive feedback.
        </p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# CALCULATOR
# ---------------------------------------------------------
elif menu == "🧮 Calculator":
    st.markdown("<h1>Carbon Footprint Calculator</h1>", unsafe_allow_html=True)

    if lottie_calc:
        st_lottie(lottie_calc, height=200)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='section-energy'>", unsafe_allow_html=True)
        if lottie_energy:
            st_lottie(lottie_energy, height=140)
        e = st.number_input("Electricity (kWh/month)", 0.0)
        lpg = st.number_input("LPG (kg/month)", 0.0)
        water = st.number_input("Water (litres/day)", 0.0)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='section-travel'>", unsafe_allow_html=True)
        if lottie_travel:
            st_lottie(lottie_travel, height=140)
        car = st.number_input("Car (km/day)", 0.0)
        bike = st.number_input("Bike (km/day)", 0.0)
        public = st.number_input("Public Transport (km/day)", 0.0)
        air = st.number_input("Air Travel (km/year)", 0.0)
        waste = st.number_input("Waste (kg/week)", 0.0)
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🌱 Calculate Footprint"):
        total, breakdown = calculate_carbon(e, lpg, car, bike, public, air, waste, water)

        if lottie_success:
            st_lottie(lottie_success, height=150)

        st.markdown("<div class='section-result'>", unsafe_allow_html=True)
        st.success(f"🌍 Total Monthly Footprint: {total:.2f} kg CO₂")

        for k, v in breakdown.items():
            pct = (v / total * 100) if total > 0 else 0
            st.write(f"**{k}: {v:.2f} kg CO₂ ({pct:.1f}%)**")
            st.markdown(
                f"<div class='progress'><div class='fill' style='width:{pct}%'></div></div>",
                unsafe_allow_html=True
            )
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------
elif menu == "ℹ️ About":
    st.markdown("<h1>About EcoTrack</h1>", unsafe_allow_html=True)

    if lottie_sustain:
        st_lottie(lottie_sustain, height=220)

    st.markdown("""
    <div class="eco-card">
    <p style="font-size:18px">
    EcoTrack is a product-based proof-of-concept showcasing how modern software
    applications can quantify environmental impact using structured user data
    and emission factors.
    </p>
    <ul>
        <li>Interactive eco-themed UI</li>
        <li>Accurate carbon estimation</li>
        <li>Visual and animated feedback</li>
        <li>Scalable system design</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
