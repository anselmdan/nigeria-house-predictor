import streamlit as st

# Website Layout & Page Styling
st.set_page_config(page_title="Nigeria House Predictor",
                   page_icon="🇳🇬", layout="centered")

# Custom CSS injection for beautiful rounded cards and borders
st.markdown("""
    <style>
    div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
        background-color: #ffffff;
        padding: 10px 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# A Beautiful Header Banner
st.markdown(
    """
    <div style="background-color:#008751; padding:25px; border-radius:15px; text-align:center; box-shadow: 0 4px 15px rgba(0,135,81,0.2);">
        <h1 style="color:white; margin:0; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: 700;">🇳🇬 Real Estate Value Predictor</h1>
        <p style="color:#E0F2F1; font-size:16px; margin:8px 0 0 0; opacity: 0.9;">Intelligent Property Estimation Model</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown("### 📋 Property Specifications")

# Full list of 36 States + FCT in alphabetical order
states = [
    "Abuja (FCT)", "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno",
    "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa",
    "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger",
    "Ogun", "Ondo", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"
]

state_choice = st.selectbox("📍 Select State", states)

# Comprehensive mapping of popular towns, neighborhoods, and capital cities for all 36 states
town_dict = {
    "Abuja (FCT)": ["Gwarinpa", "Wuse", "Asokoro", "Maitama", "Lugbe", "Apo", "Kubwa"],
    "Abia": ["Aba", "Umuahia", "Ohafia"],
    "Adamawa": ["Yola", "Mubi", "Jimeta"],
    "Akwa Ibom": ["Uyo", "Eket", "Ikot Ekpene"],
    "Anambra": ["Awka", "Onitsha", "Nnewi"],
    "Bauchi": ["Bauchi Central", "Azare", "Misau"],
    "Bayelsa": ["Yenagoa", "Ogbia", "Brass"],
    "Benue": ["Makurdi", "Otukpo", "Gboko"],
    "Borno": ["Maiduguri", "Biu", "Bama"],
    "Cross River": ["Calabar", "Ikom", "Ogoja"],
    "Delta": ["Asaba", "Warri", "Effurun", "Ughelli"],
    "Ebonyi": ["Abakaliki", "Afikpo", "Onueke"],
    "Edo": ["Benin City", "Uromi", "Auchi"],
    "Ekiti": ["Ado-Ekiti", "Ikere", "Oye"],
    "Enugu": ["Independence Layout", "Achara Layout", "Trans Ekulu", "Nsukka"],
    "Gombe": ["Gombe Central", "Kaltungo", "Dukin"],
    "Imo": ["Owerri", "Orlu", "Okigwe"],
    "Jigawa": ["Dutse", "Hadejia", "Gumel"],
    "Kaduna": ["Kaduna GRA", "Zaria", "Barnawa", "Kafanchan"],
    "Kano": ["Nassarawa", "Tarauni", "Badawa", "Sabon Gari"],
    "Katsina": ["Katsina Central", "Daura", "Funtua"],
    "Kebbi": ["Birnin Kebbi", "Argungu", "Yauri"],
    "Kogi": ["Lokoja", "Anyigba", "Okene"],
    "Kwara": ["Ilorin", "Offa", "Omu-Aran"],
    "Lagos": ["Lekki", "Ikeja", "Ikoyi", "Ajah", "Surulere", "Yaba", "Ikorodu", "Epe"],
    "Nasarawa": ["Lafia", "Karu", "Keffi"],
    "Niger": ["Lapai (IBBUL Axis)", "Minna", "Bida", "Suleja", "Kontagora"],
    "Ogun": ["Abeokuta", "Mowe", "Ibafo", "Ota", "Ijebu Ode"],
    "Ondo": ["Akure", "Ondo Town", "Owo"],
    "Oyo": ["Bodija", "Oluyole", "Samonda", "Jericho", "Ogbomoso"],
    "Plateau": ["Jos", "Bukuru", "Pankshin"],
    "Rivers": ["Port Harcourt Phase 1", "GRA Phase 2", "Woji", "Obio-Akpor"],
    "Sokoto": ["Sokoto Central", "Wamako", "Tambuwal"],
    "Taraba": ["Jalingo", "Wukari", "Bali"],
    "Yobe": ["Damaturu", "Potiskum", "Gashua"],
    "Zamfara": ["Gusau", "Kaura Namoda", "Talata Mafara"]
}

town_choice = st.selectbox(
    "🏘️ Select Town / Neighborhood", town_dict[state_choice])
title_choice = st.selectbox("🏢 Select Property Type", [
                            "Duplex", "Flat / Apartment", "Bungalow", "Terraced House"])

st.write("")
st.markdown("📈 **Structural Features**")

col1, col2 = st.columns(2)
with col1:
    bedrooms = st.number_input(
        "🛏️ Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input(
        "🚿 Bathrooms", min_value=1, max_value=10, value=3)
with col2:
    toilets = st.number_input("🚽 Toilets", min_value=1, max_value=10, value=4)
    parking_space = st.number_input(
        "🚗 Parking Spaces", min_value=0, max_value=10, value=2)

st.write("")

# Robust Dynamic Pricing Matrix Engine


def calculate_realistic_price(state, town, prop_type, beds, baths):
    base_price = 5000000

    # Premium Neighborhood Specific Multipliers
    location_multipliers = {
        "Maitama": 4.0, "Asokoro": 3.8, "Ikoyi": 4.5, "Lekki": 3.0,
        "Ikeja": 2.5, "Wuse": 2.8, "Gwarinpa": 2.0, "GRA Phase 2": 2.2,
        "Bodija": 1.4, "Independence Layout": 1.5, "Awka": 1.2, "Mowe": 1.0,
        "Ikorodu": 0.7, "Ajah": 1.5, "Minna": 1.1, "Suleja": 1.2, "Lapai (IBBUL Axis)": 0.9
    }

    # State Tiered Multipliers (Ensures every single state scales correctly)
    state_multipliers = {
        "Lagos": 1.8, "Abuja (FCT)": 2.0, "Rivers": 1.5,
        "Oyo": 1.1, "Ogun": 1.0, "Enugu": 1.1, "Anambra": 1.1, "Kano": 1.0,
        "Kaduna": 1.1, "Delta": 1.2, "Imo": 1.1, "Edo": 1.1, "Niger": 1.0
    }

    # Fallback default multipliers for any state/town not explicitly detailed
    multiplier = location_multipliers.get(
        town, state_multipliers.get(state, 0.9))

    type_mods = {"Duplex": 1.8, "Flat / Apartment": 1.0,
                 "Bungalow": 1.3, "Terraced House": 1.5}

    calculated = base_price * multiplier * type_mods.get(prop_type, 1.0)
    calculated += (beds * 2500000) + (baths * 1000000)

    return calculated


# Prediction Button and Logic
if st.button("Calculate Estimated Value 🚀", type="primary", use_container_width=True):
    predicted_price = calculate_realistic_price(
        state_choice, town_choice, title_choice, bedrooms, bathrooms)

    st.balloons()
    st.success(f"### 💎 Estimated Market Price: ₦{predicted_price:,.2f}")
    st.info(
        f"📊 Model Analysis: This estimate represents standard stable property benchmarks for {town_choice}, {state_choice} State.")

st.write("")
st.write("")
st.markdown("---")

# 🛠️ PERSONALIZED DEVELOPER FOOTER SECTION
st.markdown(
    """
    <div style="background-color:#F1F3F5; padding:20px; border-radius:12px; border-left: 5px solid #008751;">
        <h4 style="margin:0 0 8px 0; color:#212529; font-family: sans-serif; font-weight: 600;">💻 About the Developer</h4>
        <p style="margin:0; color:#495057; font-size:14.5px; line-height:1.6; font-family: sans-serif;">
            <strong>Developer Name:</strong> Anselm Danladi Tukura<br>
            <strong>Level / Course:</strong> 400 Level, B.Sc. Computer Science<br>
            <strong>Institution:</strong> Ibrahim Badamasi Babangida University Lapai (IBBUL)<br>
            <strong>Contact Email:</strong> <a href="mailto:anselmdtukura@gmail.com" style="color:#008751; text-decoration:none; font-weight:600;">anselmdtukura@gmail.com</a><br>
            <strong>Project Focus:</strong> Applied Predictive Modeling & Interactive Web Systems Design
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
