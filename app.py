import streamlit as st
import math

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="All-in-One Converter",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- DATA & CONSTANTS ---
# Expanded unit categories with base units for consistency
# Base unit for most is the standard SI unit (e.g., Meters, Kilograms, etc.)
UNIT_CATEGORIES = {
    "Length": {
        "units": {
            "Meters (m)": 1.0, "Centimeters (cm)": 0.01, "Millimeters (mm)": 0.001,
            "Kilometers (km)": 1000.0, "Inches (in)": 0.0254, "Feet (ft)": 0.3048,
            "Yards (yd)": 0.9144, "Miles (mi)": 1609.34, "Micrometers (µm)": 1e-6,
            "Nanometers (nm)": 1e-9, "Angstroms (Å)": 1e-10, "Light Years (ly)": 9.461e15
        }, "icon": "📏"
    },
    "Mass": {
        "units": {
            "Kilograms (kg)": 1.0, "Grams (g)": 0.001, "Milligrams (mg)": 1e-6,
            "Tonnes (t)": 1000.0, "Pounds (lb)": 0.453592, "Ounces (oz)": 0.0283495,
            "Carats (ct)": 0.0002
        }, "icon": "⚖️"
    },
    "Area": {
        "units": {
            "Square Meters (m²)": 1.0, "Square Centimeters (cm²)": 1e-4, "Square Kilometers (km²)": 1e6,
            "Hectares (ha)": 10000.0, "Square Feet (ft²)": 0.092903, "Acres (ac)": 4046.86,
            "Square Miles (mi²)": 2.59e6
        }, "icon": "📐"
    },
    "Volume": {
        "units": {
            "Cubic Meters (m³)": 1.0, "Liters (L)": 0.001, "Milliliters (mL)": 1e-6,
            "Cubic Centimeters (cm³)": 1e-6, "Cubic Feet (ft³)": 0.0283168,
            "US Gallons (gal)": 0.00378541, "US Quarts (qt)": 0.000946353
        }, "icon": "🧊"
    },
    "Data": {
        "units": {
            "Bits (b)": 1.0, "Bytes (B)": 8.0, "Kilobits (kb)": 1000.0,
            "Kilobytes (kB)": 8000.0, "Megabits (Mb)": 1e6, "Megabytes (MB)": 8e6,
            "Gigabits (Gb)": 1e9, "Gigabytes (GB)": 8e9, "Terabits (Tb)": 1e12,
            "Terabytes (TB)": 8e12
        }, "icon": "💾"
    },
    "Force": {
        "units": {
            "Newtons (N)": 1.0, "Kilonewtons (kN)": 1000.0, "Pounds-force (lbf)": 4.44822,
            "Dynes (dyn)": 1e-5, "Kilogram-force (kgf)": 9.80665
        }, "icon": "💪"
    },
    "Pressure": {
        "units": {
            "Pascals (Pa)": 1.0, "Kilopascals (kPa)": 1000.0, "Bar": 100000.0,
            "Atmospheres (atm)": 101325.0, "Millimeters of Mercury (mmHg)": 133.322,
            "Pounds per Square Inch (psi)": 6894.76
        }, "icon": "🎚️"
    },
    "Energy": {
        "units": {
            "Joules (J)": 1.0, "Kilojoules (kJ)": 1000.0, "Calories (cal)": 4.184,
            "Kilocalories (kcal)": 4184.0, "Watt-hours (Wh)": 3600.0,
            "Kilowatt-hours (kWh)": 3.6e6, "Electronvolts (eV)": 1.60218e-19,
            "British Thermal Unit (BTU)": 1055.06
        }, "icon": "🔋"
    },
    "Power": {
        "units": {
            "Watts (W)": 1.0, "Kilowatts (kW)": 1000.0, "Megawatts (MW)": 1e6,
            "Horsepower (hp)": 745.7, "BTU/hour": 0.293071
        }, "icon": "⚡"
    },
    "Voltage": {
        "units": { "Volts (V)": 1.0, "Millivolts (mV)": 0.001, "Kilovolts (kV)": 1000.0 },
        "icon": "⚡"
    },
    "Electric Current": {
        "units": { "Amperes (A)": 1.0, "Milliamperes (mA)": 0.001, "Kiloamperes (kA)": 1000.0 },
        "icon": "🔌"
    },
    "Resistance": {
        "units": { "Ohms (Ω)": 1.0, "Kiloohms (kΩ)": 1000.0, "Megaohms (MΩ)": 1e6 },
        "icon": "🔩"
    },
    "Frequency": {
        "units": { "Hertz (Hz)": 1.0, "Kilohertz (kHz)": 1000.0, "Megahertz (MHz)": 1e6, "Gigahertz (GHz)": 1e9 },
        "icon": "🎵"
    },
    # Add other categories as needed
}

# --- CUSTOM CSS ---
def load_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        background-attachment: fixed;
    }
    .main-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.20);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    .result-box {
        background-color: #e0f7fa;
        border-left: 7px solid #00bcd4;
        color: #004d40;
        padding: 1.5rem;
        border-radius: 11px;
        margin-top: 20px;
        text-align: center;
    }
    .result-text {
        font-size: 1.65rem;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UNIT CONVERTER ---
def render_standard_converter(category_name):
    category = UNIT_CATEGORIES[category_name]
    if category_name == "Temperature":
        units = category["units"]
    else:
        units = list(category["units"].keys())

    st.header(f"{category['icon']} {category_name} Converter")
    from_unit = st.selectbox("From Unit", units, key=f"from_{category_name}")
    to_unit = st.selectbox("To Unit", units, key=f"to_{category_name}")
    value = st.number_input("Enter Value", value=1.0, format="%.8f")

    # Temperature Conversion
    if category_name == "Temperature":
        result = temp_convert(value, from_unit, to_unit)
    else:
        # General unit conversion
        base_val = value * category["units"][from_unit]
        result = base_val / category["units"][to_unit]

    st.markdown(f"**{value} {from_unit} = {result:.8f} {to_unit}**")

def temp_convert(val, from_unit, to_unit):
    # Convert from source to Celsius first
    if from_unit == "Celsius (°C)":
        c = val
    elif from_unit == "Fahrenheit (°F)":
        c = (val - 32) * 5/9
    else:  # Kelvin
        c = val - 273.15
    # Convert from Celsius to target unit
    if to_unit == "Celsius (°C)":
        return c
    elif to_unit == "Fahrenheit (°F)":
        return c * 9/5 + 32
    else:  # Kelvin
        return c + 273.15

# --- BMI CALCULATOR ---
def render_bmi_calculator():
    st.header("🏋️ BMI Calculator")
    weight = st.number_input("Weight (kg)", min_value=0.0, value=70.0, format="%.2f")
    height_cm = st.number_input("Height (cm)", min_value=0.0, value=170.0, format="%.2f")
    height_m = height_cm / 100
    if st.button("Calculate BMI"):
        bmi = weight / (height_m ** 2) if height_m > 0 else 0
        st.success(f"Your BMI = {bmi:.2f}")
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif bmi < 24.9:
            st.info("Category: Normal weight")
        elif bmi < 29.9:
            st.info("Category: Overweight")
        else:
            st.info("Category: Obese")

# --- REACTANCE & SUSCEPTANCE CALCULATOR ---
def render_reactance_susceptance_calculator():
    st.header("⚛️ Reactance & Susceptance Calculators")
    calc_mode = st.radio("Choose Calculation", [
        "Inductive Reactance (from L, f)", "Inductance (from X, f)",
        "Capacitive Reactance (from C, f)", "Capacitance (from Xc, f)",
        "Susceptance (B) from Capacitance", "Capacitance from Susceptance"
    ], horizontal=True)

    if calc_mode == "Inductive Reactance (from L, f)":
        L = st.number_input("Enter Inductance (H)", min_value=0.0, value=0.01, format="%.6f")
        f = st.number_input("Enter Frequency (Hz)", min_value=0.0, value=50.0, format="%.2f")
        Xl = 2 * math.pi * f * L
        st.markdown(f'**Inductive Reactance Xₗ = {Xl:.4f} Ω**')

    elif calc_mode == "Inductance (from X, f)":
        Xl = st.number_input("Enter Inductive Reactance (Ω)", min_value=0.0, value=10.0, format="%.4f")
        f = st.number_input("Enter Frequency (Hz)", min_value=1e-6, value=50.0, format="%.2f")
        L = Xl / (2 * math.pi * f) if f > 0 else 0
        st.markdown(f'**Inductance L = {L:.6f} H**')

    elif calc_mode == "Capacitive Reactance (from C, f)":
        C = st.number_input("Enter Capacitance (F)", min_value=1e-12, value=1e-6, format="%.10f")
        f = st.number_input("Enter Frequency (Hz)", min_value=0.0, value=50.0, format="%.2f")
        Xc = 1 / (2 * math.pi * f * C) if f > 0 and C > 0 else 0
        st.markdown(f'**Capacitive Reactance Xc = {Xc:.4f} Ω**')

    elif calc_mode == "Capacitance (from Xc, f)":
        Xc = st.number_input("Enter Capacitive Reactance (Ω)", min_value=1e-9, value=10.0, format="%.4f")
        f = st.number_input("Enter Frequency (Hz)", min_value=1e-6, value=50.0, format="%.2f")
        C = 1 / (2 * math.pi * f * Xc) if f > 0 and Xc > 0 else 0
        st.markdown(f'**Capacitance C = {C:.8f} F**')

    elif calc_mode == "Susceptance (B) from Capacitance":
        C = st.number_input("Enter Capacitance (F)", min_value=1e-12, value=1e-6, format="%.10f")
        f = st.number_input("Enter Frequency (Hz)", min_value=0.0, value=50.0, format="%.2f")
        B = 2 * math.pi * f * C
        st.markdown(f'**Susceptance B = {B:.8f} S**')

    elif calc_mode == "Capacitance from Susceptance":
        B = st.number_input("Enter Susceptance (S)", min_value=1e-12, value=1e-6, format="%.10f")
        f = st.number_input("Enter Frequency (Hz)", min_value=1e-6, value=50.0, format="%.2f")
        C = B / (2 * math.pi * f) if f > 0 else 0
        st.markdown(f'**Capacitance C = {C:.8f} F**')

# --- CAPACITANCE CONVERTER ---
def render_capacitance_converter():
    st.header("💡 Capacitance Converter")
    category = UNIT_CATEGORIES["Capacitance"]
    units = list(category["units"].keys())
    from_unit = st.selectbox("From Unit", units, key="from_cap")
    to_unit = st.selectbox("To Unit", units, key="to_cap")
    value = st.number_input("Enter Capacitance Value", value=1.0, format="%.8f")
    base_val = value * category["units"][from_unit]
    result = base_val / category["units"][to_unit]
    st.markdown(f'**{value} {from_unit} = {result:.8f} {to_unit}**')

# --- ENHANCED PER UNIT SYSTEM CALCULATOR ---
def render_enhanced_per_unit_calculator():
    st.header("⚡ Enhanced Per-Unit (PU) System Calculator")
    st.info("Advanced PU calculations for Resistance, Reactance, Susceptance (including per km inputs).")

    st.subheader("System Base Values")
    col1, col2 = st.columns(2)
    base_mva = col1.number_input("Base MVA (S_base)", min_value=0.1, value=100.0, format="%.2f")
    base_kv = col2.number_input("Base Voltage (V_base, Line-to-Line)", min_value=0.1, value=13.8, format="%.2f")

    z_base = (base_kv ** 2) / base_mva
    i_base = (base_mva * 1000) / (math.sqrt(3) * base_kv)

    with st.expander("Derived Base Values", expanded=True):
        st.metric(label="Base Impedance (Z_base)", value=f"{z_base:.4f} Ω")
        st.metric(label="Base Current (I_base)", value=f"{i_base:.4f} A")

    st.markdown("---")
    st.subheader("Enter Actual Values or Per Kilometer Values")
    calc_type = st.radio("Choose Parameter", [
        "Impedance (Ω)", "Resistance (Ω)", "Reactance (Ω)", "Susceptance (S)"
    ], horizontal=True)

    per_km = st.checkbox("Input as per km value?")
    if per_km:
        val_per_km = st.number_input(f"Value per km ({calc_type})", min_value=0.0, value=0.05, format="%.6f")
        total_km = st.number_input("Total Length (km)", min_value=0.1, value=10.0, format="%.2f")
        actual_val = val_per_km * total_km
    else:
        actual_val = st.number_input(f"Total Value ({calc_type})", min_value=0.0, value=0.5, format="%.6f")

    if st.button("Convert to Per-Unit", use_container_width=True):
        if calc_type in ["Impedance (Ω)", "Resistance (Ω)", "Reactance (Ω)"]:
            pu_val = actual_val / z_base if z_base > 0 else 0
            st.success(f"Per-Unit {calc_type.split()[0]} = {pu_val:.6f} pu")
        elif calc_type == "Susceptance (S)":
            b_base = 1 / z_base if z_base > 0 else 0
            pu_val = actual_val / b_base if b_base > 0 else 0
            st.success(f"Per-Unit Susceptance = {pu_val:.6f} pu")

# --- ZIP LOAD MODEL CALCULATOR ---
def render_zip_load_calculator():
    st.header("🔌 ZIP Load Model Calculator")
    st.write("The ZIP model expresses load as a mix of constant Impedance (Z), Current (I), and Power (P) terms:")
    st.latex(r"P_{load}=P_0 (a_z V^2 + a_i V + a_p)")
    st.latex(r"Q_{load}=Q_0 (b_z V^2 + b_i V + b_p)")

    st.subheader("Coefficients (sum must be 1 for each set):")
    az = st.slider("Impedance (a_z)", 0.0, 1.0, 0.3, 0.01)
    ai = st.slider("Current (a_i)", 0.0, 1.0, 0.3, 0.01)
    ap = st.slider("Power (a_p)", 0.0, 1.0, 0.4, 0.01)
    if round(az + ai + ap, 2) != 1.0:
        st.error("a_z + a_i + a_p must sum to 1")

    bz = st.slider("Impedance (b_z)", 0.0, 1.0, 0.3, 0.01)
    bi = st.slider("Current (b_i)", 0.0, 1.0, 0.3, 0.01)
    bp = st.slider("Power (b_p)", 0.0, 1.0, 0.4, 0.01)
    if round(bz + bi + bp, 2) != 1.0:
        st.error("b_z + b_i + b_p must sum to 1")

    st.subheader("Base Load & Voltage Inputs:")
    p0 = st.number_input("P₀ (Base Active Power, kW)", value=100.0, format="%.3f")
    q0 = st.number_input("Q₀ (Base Reactive Power, kVAR)", value=50.0, format="%.3f")
    v = st.number_input("Voltage (per unit)", min_value=0.0, value=1.0, format="%.3f")

    if st.button("Calculate ZIP Load", key="calc_zip"):
        p_load = p0 * (az * v**2 + ai * v + ap)
        q_load = q0 * (bz * v**2 + bi * v + bp)
        st.success(f"Active Power P_load = {p_load:.4f} kW")
        st.info(f"Reactive Power Q_load = {q_load:.4f} kVAR")

# --- MAIN APP LAYOUT ---
load_css()
st.title("🌟 Enhanced All-in-One Engineering & Science Converter")

st.sidebar.title("Navigation")
app_mode = st.sidebar.radio(
    "Choose a Calculator",
    [
        "Unit Converter", "🌡️ Temperature", "🏋️ BMI Calculator", "⚡ Per-Unit System",
        "⚛️ Reactance & Susceptance", "💡 Capacitance Converter", "🔌 ZIP Load Model"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This enhanced app provides a diverse collection of interactive scientific, engineering, and power system tools with a modern, visually appealing design."
)

# --- APP MODE SELECTION ---
if app_mode == "Unit Converter":
    category_names = list(UNIT_CATEGORIES.keys())
    selected_category = st.radio("Select Conversion Category:", category_names, horizontal=True)
    render_standard_converter(selected_category)

elif app_mode == "🌡️ Temperature":
    render_standard_converter("Temperature")

elif app_mode == "🏋️ BMI Calculator":
    render_bmi_calculator()

elif app_mode == "⚡ Per-Unit System":
    render_enhanced_per_unit_calculator()

elif app_mode == "⚛️ Reactance & Susceptance":
    render_reactance_susceptance_calculator()

elif app_mode == "💡 Capacitance Converter":
    render_capacitance_converter()

elif app_mode == "🔌 ZIP Load Model":
    render_zip_load_calculator()
