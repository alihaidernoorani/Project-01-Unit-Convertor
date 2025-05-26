import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="wide",
)

st.title("📏 Unit Converter")

# Conversion categories
conversion_list = [
    "Length", "Area", "Volume", "Mass", "Speed",
    "Time", "Pressure", "Energy", "Digital Storage"
]

# Conversion dictionaries (relative to base units)
length_conversions = {
    "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
    "Micrometer": 1_000_000, "Nanometer": 1_000_000_000, "Mile": 0.000621371,
    "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701, "Nautical Mile": 0.000539957,
}

area_conversions = {
    "Square Meter": 1, "Square Kilometer": 1e-6, "Square Centimeter": 10_000,
    "Square Millimeter": 1_000_000, "Square Mile": 3.861e-7, "Square Yard": 1.19599,
    "Square Foot": 10.7639, "Square Inch": 1550.0031, "Acre": 0.000247105, "Hectare": 0.0001,
}

volume_conversions = {
    "Cubic Meter": 1, "Cubic Kilometer": 1e-9, "Cubic Centimeter": 1_000_000,
    "Cubic Millimeter": 1_000_000_000, "Liter": 1_000, "Milliliter": 1_000_000,
    "Cubic Inch": 61.0237, "Cubic Foot": 35.3147, "Cubic Yard": 1.30795,
    "Gallon (US)": 264.172, "Quart (US)": 1056.69, "Pint (US)": 2113.38,
    "Cup (US)": 4226.75, "Fluid Ounce (US)": 33814,
}

mass_conversions = {
    "Kilogram": 1, "Gram": 1_000, "Milligram": 1_000_000, "Microgram": 1_000_000_000,
    "Metric Ton": 0.001, "Long Ton (UK)": 0.000984207, "Short Ton (US)": 0.00110231,
    "Pound": 2.20462, "Ounce": 35.274, "Carat": 5000, "Stone (UK)": 0.157473,
}

speed_conversions = {
    "Meter per Second": 1, "Kilometer per Hour": 3.6, "Mile per Hour": 2.23694,
    "Foot per Second": 3.28084, "Knot (Nautical Mile per Hour)": 1.94384,
}

time_conversions = {
    "Second": 1, "Millisecond": 1_000, "Microsecond": 1_000_000, "Nanosecond": 1_000_000_000,
    "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400, "Week": 1/604800,
    "Month (30 days)": 1/2.628e6, "Year": 1/3.154e7,
}

pressure_conversions = {
    "Pascal": 1, "Kilopascal": 0.001, "Bar": 1e-5, "Atmosphere": 9.8692e-6,
    "Torr (mmHg)": 0.00750062, "Pound per Square Inch (PSI)": 0.000145038,
}

energy_conversions = {
    "Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006, "Kilocalorie": 0.000239006,
    "Watt-hour": 0.000277778, "Kilowatt-hour": 2.7778e-7,
    "Electron Volt": 6.242e+18, "British Thermal Unit (BTU)": 0.000947817,
    "Foot-Pound": 0.737562,
}

storage_conversions = {
    "Bit": 1, "Byte": 1/8, "Kilobit": 1/1_000, "Kilobyte": 1/8_000,
    "Megabit": 1/1_000_000, "Megabyte": 1/8_000_000,
    "Gigabit": 1/1_000_000_000, "Gigabyte": 1/8_000_000_000,
    "Terabit": 1/1_000_000_000_000, "Terabyte": 1/8_000_000_000_000,
    "Petabyte": 1/8_000_000_000_000_000,
}

# Mapping categories to their unit dictionaries
unit_mappings = {
    "Length": length_conversions,
    "Area": area_conversions,
    "Volume": volume_conversions,
    "Mass": mass_conversions,
    "Speed": speed_conversions,
    "Time": time_conversions,
    "Pressure": pressure_conversions,
    "Energy": energy_conversions,
    "Digital Storage": storage_conversions,
}

# Dropdown for conversion type
option = st.selectbox("Select a Category", conversion_list)

# Get units for the selected type
unit_options = list(unit_mappings[option].keys())

# Layout columns
col1, col2, col3 = st.columns([3, 1, 3])

with col1:
    from_unit = st.selectbox("From Unit", unit_options)
    input_value = st.number_input("Enter Value", value=1.0)

with col2:
    st.markdown("<h2 style='text-align: center;'>→</h2>", unsafe_allow_html=True)

with col3:
    to_unit = st.selectbox("To Unit", unit_options)

    # Perform conversion
    result = input_value * unit_mappings[option][to_unit] / unit_mappings[option][from_unit]
    st.text_input("Converted Value", value=round(result, 6), disabled=True)

    st.caption(f"{input_value} {from_unit} = {round(result, 6)} {to_unit}")