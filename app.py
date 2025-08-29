import streamlit as st
unit_categories = {
"Length": {
"units": {
"Meters (m)": 1.0,
"Centimeters (cm)": 0.01,
"Millimeters (mm)": 0.001,
"Kilometers (km)": 1000.0,
"Inches (in)": 0.0254,
"Feet (ft)": 0.3048,
"Yards (yd)": 0.9144,
"Miles (mi)": 1609.34
},
"icon": "📏"
},
"Mass": {
"units": {
"Kilograms (kg)": 1.0,
"Grams (g)": 0.001,
"Milligrams (mg)": 0.000001,
"Tonnes (t)": 1000.0,
"Pounds (lb)": 0.453592,
"Ounces (oz)": 0.0283495
},
"icon": "⚖️"
},
"Temperature": {
"units": {
"Celsius (°C)": "c",
"Fahrenheit (°F)": "f",
"Kelvin (K)": "k"
},
"icon": "🌡️"
},
"Time": {
"units": {
"Seconds (s)": 1.0,
"Minutes (min)": 60.0,
"Hours (h)": 3600.0,
"Days (d)": 86400.0
},
"icon": "⏰"
},
"Area": {
"units": {
"Square Meters (m²)": 1.0,
"Square Centimeters (cm²)": 0.0001,
"Square Millimeters (mm²)": 0.000001,
"Square Kilometers (km²)": 1e6,
"Hectares (ha)": 10000.0,
"Square Feet (ft²)": 0.092903,
"Square Yards (yd²)": 0.836127,
"Acres (ac)": 4046.86,
"Square Miles (mi²)": 2.59e6
},
"icon": "📐"
},
"Volume": {
"units": {
"Cubic Meters (m³)": 1.0,
"Liters (L)": 0.001,
"Milliliters (mL)": 0.000001,
"Cubic Centimeters (cm³)": 0.000001,
"Cubic Millimeters (mm³)": 1e-9,
"Cubic Inches (in³)": 1.6387e-5,
"Cubic Feet (ft³)": 0.0283168,
"Cubic Yards (yd³)": 0.764555,
"Gallons (US gal)": 0.00378541,
"Quarts (US qt)": 0.000946353
},
"icon": "🧊"
},
"Force": {
"units": {
"Newtons (N)": 1.0,
"Kilonewtons (kN)": 1000.0,
"Pounds-force (lbf)": 4.44822,
"Dynes (dyn)": 1e-5
},
"icon": "💪"
},
"Pressure": {
"units": {
"Pascals (Pa)": 1.0,
"Kilopascals (kPa)": 1000.0,
"Bar": 100000.0,
"Atmospheres (atm)": 101325.0,
"Millimeters of Mercury (mmHg)": 133.322,
"Pounds per Square Inch (psi)": 6894.76
},
"icon": "🎚️"
},
"Energy": {
"units": {
"Joules (J)": 1.0,
"Kilojoules (kJ)": 1000.0,
"Calories (cal)": 4.184,
"Kilocalories (kcal)": 4184.0,
"Watt-hours (Wh)": 3600.0,
"Kilowatt-hours (kWh)": 3.6e6,
"Electronvolts (eV)": 1.60218e-19
},
"icon": "🔋"
},
"Power": {
"units": {
"Watts (W)": 1.0,
"Kilowatts (kW)": 1000.0,
"Horsepower (hp)": 745.7,
"BTU/h": 0.293071
},
"icon": "⚡"
},
"Electric Current": {
"units": {
"Amperes (A)": 1.0,
"Milliamperes (mA)": 0.001,
"Kiloamperes (kA)": 1000.0
},
"icon": "🔌"
},
"Voltage": {
"units": {
"Volts (V)": 1.0,
"Millivolts (mV)": 0.001,
"Kilovolts (kV)": 1000.0
},
"icon": "🔋"
},
"Resistance": {
"units": {
"Ohms (Ω)": 1.0,
"Kiloohms (kΩ)": 1000.0,
"Megaohms (MΩ)": 1e6
},
"icon": "🔩"
},
"Capacitance": {
"units": {
"Farads (F)": 1.0,
"Millifarads (mF)": 0.001,
"Microfarads (μF)": 1e-6,
"Nanofarads (nF)": 1e-9,
"Picofarads (pF)": 1e-12
},
"icon": "🪫"
},
"Inductance": {
"units": {
"Henrys (H)": 1.0,
"Millihenrys (mH)": 0.001,
"Microhenrys (μH)": 1e-6
},
"icon": "🧲"
},
"Frequency": {
"units": {
"Hertz (Hz)": 1.0,
"Kilohertz (kHz)": 1000.0,
"Megahertz (MHz)": 1e6,
"Gigahertz (GHz)": 1e9
},
"icon": "🎵"
},
"Data": {
"units": {
"Bits (b)": 1.0,
"Bytes (B)": 8.0,
"Kilobits (kb)": 1000.0,
"Kilobytes (kB)": 8000.0,
"Megabits (Mb)": 1e6,
"Megabytes (MB)": 8e6,
"Gigabits (Gb)": 1e9,
"Gigabytes (GB)": 8e9,
"Terabits (Tb)": 1e12,
"Terabytes (TB)": 8e12
},
"icon": "💾"
},
"Angle": {
"units": {
"Degrees (°)": 1.0,
"Radians (rad)": 57.2958,
"Gradians (gon)": 0.9
},
"icon": "📐"
}
}
st.markdown("""
.stApp {
background: linear-gradient(120deg,#cbe7f6,#f7cac9,#ffe193,#c1fba4,#d0c7f6);
background-attachment: fixed;
}
.big-font {
font-size:2rem !important;
font-weight:bold;
color:#003366;
}
.unit-box {
background-color: #ffffffcc;
padding: 1.5em;
border-radius: 16px;
box-shadow: 0 2px 12px #21212120;
margin-bottom: 2em;
}
""", unsafe_allow_html=True)
st.markdown('🌟 All-in-One Unit Converter 🌟', unsafe_allow_html=True)
st.write("#### Powered by Streamlit")
st.write("Convert units across Science, Engineering, and Mathematics disciplines. Simply select a category, enter a value, and choose your units!")
category = st.selectbox(
"Select a conversion category:",
list(unit_categories.keys()),
index=0
)
icon = unit_categories[category]["icon"]
with st.container():
    st.markdown(f'{icon} {category} Unit Conversion', unsafe_allow_html=True)
    if category == "Temperature":
        temp_units = list(unit_categories["Temperature"]["units"].keys())
        from_unit = st.selectbox("From:", temp_units, index=0)
        to_unit = st.selectbox("To:", temp_units, index=1)
        value = st.number_input("Value:", value=0.0, format="%.3f", key="temp_in")
        def convert_temperature(val, u_from, u_to):
            if u_from == u_to:
                return val
            # Convert from input to Celsius
            if u_from == "Celsius (°C)":
                c = val
            elif u_from == "Fahrenheit (°F)":
                c = (val - 32) * 5.0 / 9.0
            elif u_from == "Kelvin (K)":
                c = val - 273.15
            else:
                c = val
            # Convert from Celsius to output
            if u_to == "Celsius (°C)":
                return c
            elif u_to == "Fahrenheit (°F)":
                return c * 9.0 / 5.0 + 32
            elif u_to == "Kelvin (K)":
                return c + 273.15
            return c
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    else:
        units = list(unit_categories[category]["units"].keys())
        from_unit = st.selectbox("From:", units, index=0)
        to_unit = st.selectbox("To:", units, index=1)
        value = st.number_input("Value:", value=0.0, format="%.6f", key="num_in")
        base_val = value * unit_categories[category]["units"][from_unit]
        result = base_val / unit_categories[category]["units"][to_unit]
        st.success(f"{value} {from_unit} = {result:.6g} {to_unit}")
st.markdown("---")
st.info(
"✨ This app supports conversions for: Length, Mass, Temperature, Time, Area, Volume, Force, Pressure, Energy, Power, Electric Current, Voltage, Resistance, Capacitance, Inductance, Frequency, Data, and Angle! "
"If you have suggestions or want more features, let us know. Enjoy converting! 🚀"
)
