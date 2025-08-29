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

# --- STYLES ---
def load_css():
    st.markdown("""
    <style>
        /* Main App background */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            background-attachment: fixed;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(10px);
        }

        /* Main content card */
        .main-container {
            background-color: rgba(255, 255, 255, 0.7);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }

        /* Result display box */
        .result-box {
            background-color: #e0f2f1; /* Light teal background */
            border-left: 6px solid #00796b; /* Darker teal border */
            color: #004d40; /* Dark teal text */
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 20px;
            text-align: center;
        }

        .result-text {
            font-size: 1.75rem;
            font-weight: 600;
        }

    </style>
    """, unsafe_allow_html=True)

# --- CONVERTER FUNCTIONS ---

def render_standard_converter(category_name):
    """Renders the UI for standard unit conversions."""
    category = UNIT_CATEGORIES[category_name]
    icon = category["icon"]
    st.header(f"{icon} {category_name} Converter")

    units = list(category["units"].keys())
    
    col1, col2, col3 = st.columns([2, 1, 2])

    with col1:
        from_unit = st.selectbox("From Unit", units, key=f"from_{category_name}")
        value = st.number_input("Enter Value", value=1.0, format="%.6f", key=f"val_{category_name}")
        
    with col2:
        st.markdown("<div style='text-align: center; font-size: 2.5rem; margin-top: 45px;'>➡️</div>", unsafe_allow_html=True)
    
    with col3:
        to_unit = st.selectbox("To Unit", units, index=1, key=f"to_{category_name}")
    
    # Perform conversion
    if from_unit and to_unit and value is not None:
        try:
            # Convert input value to the base unit
            base_value = value * category["units"][from_unit]
            # Convert from base unit to the target unit
            result = base_value / category["units"][to_unit]

            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(f'<p class="result-text">{value:.4f} {from_unit} = {result:.6g} {to_unit}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        except ZeroDivisionError:
            st.error("Conversion factor for the target unit is zero. Cannot perform conversion.")


def render_temperature_converter():
    """Renders the UI for temperature conversion."""
    st.header("🌡️ Temperature Converter")
    
    temp_units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        from_unit = st.selectbox("From Unit", temp_units, key="from_temp")
        value = st.number_input("Enter Temperature", value=0.0, format="%.2f", key="val_temp")
        
    with col2:
        st.markdown("<div style='text-align: center; font-size: 2.5rem; margin-top: 45px;'>➡️</div>", unsafe_allow_html=True)
    
    with col3:
        to_unit = st.selectbox("To Unit", temp_units, index=1, key="to_temp")

    # Conversion logic
    if from_unit == to_unit:
        result = value
    else:
        # First, convert from source to Celsius
        if from_unit == "Fahrenheit (°F)":
            celsius = (value - 32) * 5.0 / 9.0
        elif from_unit == "Kelvin (K)":
            celsius = value - 273.15
        else: # from_unit is Celsius
            celsius = value
        
        # Then, convert from Celsius to target
        if to_unit == "Fahrenheit (°F)":
            result = (celsius * 9.0 / 5.0) + 32
        elif to_unit == "Kelvin (K)":
            result = celsius + 273.15
        else: # to_unit is Celsius
            result = celsius
            
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.markdown(f'<p class="result-text">{value:.2f} {from_unit} = {result:.2f} {to_unit}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def render_bmi_calculator():
    """Renders the UI for BMI calculation."""
    st.header("🏋️ Body Mass Index (BMI) Calculator")
    st.info("BMI is a measure of body fat based on height and weight.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_unit = st.radio("Weight Unit", ["Kilograms (kg)", "Pounds (lb)"])
        weight = st.number_input("Enter Your Weight", min_value=0.0, value=70.0, format="%.2f")
        
    with col2:
        height_unit = st.radio("Height Unit", ["Centimeters (cm)", "Meters (m)", "Feet & Inches"])
        if height_unit == "Feet & Inches":
            h_ft = st.number_input("Feet", min_value=0, value=5)
            h_in = st.number_input("Inches", min_value=0, value=9)
            # Convert feet and inches to meters
            height_m = (h_ft * 12 + h_in) * 0.0254
        else:
            height = st.number_input(f"Enter Your Height in {height_unit.split(' ')[0]}", min_value=0.0, value=175.0 if height_unit == "Centimeters (cm)" else 1.75, format="%.2f")
            # Convert height to meters
            height_m = height / 100 if height_unit == "Centimeters (cm)" else height

    # Convert weight to kg
    weight_kg = weight * 0.453592 if weight_unit == "Pounds (lb)" else weight
    
    if st.button("Calculate BMI", use_container_width=True):
        if height_m > 0 and weight_kg > 0:
            bmi = weight_kg / (height_m ** 2)
            
            # Determine BMI category
            if bmi < 18.5:
                category = "Underweight"
                color = "blue"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
                color = "green"
            elif 25 <= bmi < 30:
                category = "Overweight"
                color = "orange"
            else:
                category = "Obese"
                color = "red"
            
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(f'<p class="result-text">Your BMI is {bmi:.2f}</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="color:{color}; font-size:1.2rem; font-weight:bold;">Category: {category}</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter valid weight and height.")


def render_per_unit_calculator():
    """Renders the UI for Per Unit calculations in electrical engineering."""
    st.header("⚡ Per-Unit (PU) System Calculator")
    st.info("A tool for power system analysis. All calculations assume a three-phase system.")
    
    st.subheader("System Base Values")
    col1, col2 = st.columns(2)
    with col1:
        base_mva = st.number_input("Base MVA (S_base)", min_value=0.1, value=100.0, format="%.2f")
    with col2:
        base_kv = st.number_input("Base Voltage (V_base, Line-to-Line)", min_value=0.1, value=13.8, format="%.2f")

    # Calculate derived base values
    if base_mva > 0 and base_kv > 0:
        z_base = (base_kv ** 2) / base_mva
        i_base = (base_mva * 1000) / (math.sqrt(3) * base_kv)
        
        with st.expander("Derived Base Values", expanded=True):
            st.metric(label="Base Impedance (Z_base)", value=f"{z_base:.4f} Ω")
            st.metric(label="Base Current (I_base)", value=f"{i_base:.4f} A")
    
    st.markdown("---")
    
    calc_type = st.selectbox("Choose Conversion Type", ["Actual Value to Per-Unit", "Per-Unit to Actual Value"])
    
    if calc_type == "Actual Value to Per-Unit":
        st.subheader("Convert Actual Value to PU")
        param_type = st.radio("Select Parameter", ["Impedance (Ω)", "Current (A)", "Voltage (kV)"])
        
        if param_type == "Impedance (Ω)":
            actual_val = st.number_input("Actual Impedance (Z_actual) in Ω", value=z_base*0.05, format="%.4f")
            pu_val = actual_val / z_base if z_base > 0 else 0
            st.success(f"Per-Unit Impedance = {pu_val:.6f} pu")
            
        elif param_type == "Current (A)":
            actual_val = st.number_input("Actual Current (I_actual) in A", value=i_base, format="%.4f")
            pu_val = actual_val / i_base if i_base > 0 else 0
            st.success(f"Per-Unit Current = {pu_val:.6f} pu")
            
        elif param_type == "Voltage (kV)":
            actual_val = st.number_input("Actual Voltage (V_actual) in kV (L-L)", value=base_kv, format="%.4f")
            pu_val = actual_val / base_kv if base_kv > 0 else 0
            st.success(f"Per-Unit Voltage = {pu_val:.6f} pu")

    else: # Per-Unit to Actual Value
        st.subheader("Convert PU to Actual Value")
        param_type = st.radio("Select Parameter", ["Impedance (pu)", "Current (pu)", "Voltage (pu)"])

        if param_type == "Impedance (pu)":
            pu_val = st.number_input("Per-Unit Impedance (Z_pu)", value=0.05, format="%.6f")
            actual_val = pu_val * z_base
            st.success(f"Actual Impedance = {actual_val:.4f} Ω")

        elif param_type == "Current (pu)":
            pu_val = st.number_input("Per-Unit Current (I_pu)", value=1.0, format="%.6f")
            actual_val = pu_val * i_base
            st.success(f"Actual Current = {actual_val:.4f} A")

        elif param_type == "Voltage (pu)":
            pu_val = st.number_input("Per-Unit Voltage (V_pu)", value=1.0, format="%.6f")
            actual_val = pu_val * base_kv
            st.success(f"Actual Voltage = {actual_val:.4f} kV (L-L)")


# --- MAIN APP LAYOUT ---
load_css()

st.title("🌟 All-in-One Engineering & Science Converter")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio(
    "Choose a Calculator",
    ["Unit Converter", "🌡️ Temperature", "🏋️ BMI Calculator", "⚡ Per-Unit System"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This app provides tools for a wide range of conversions and calculations across various scientific and engineering disciplines."
)

# --- MAIN CONTENT AREA ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    if app_mode == "Unit Converter":
        st.header("Select a Category")
        # Create a grid for category selection
        category_names = list(UNIT_CATEGORIES.keys())
        cols = st.columns(4)
        selected_category = category_names[0] # Default
        
        # Using radio buttons for a cleaner selection interface
        selected_category = st.radio(
            "Conversion Category:",
            category_names,
            horizontal=True,
            label_visibility="collapsed"
        )
        st.markdown("---")
        render_standard_converter(selected_category)
        
    elif app_mode == "🌡️ Temperature":
        render_temperature_converter()
        
    elif app_mode == "🏋️ BMI Calculator":
        render_bmi_calculator()
        
    elif app_mode == "⚡ Per-Unit System":
        render_per_unit_calculator()

    st.markdown('</div>', unsafe_allow_html=True)
