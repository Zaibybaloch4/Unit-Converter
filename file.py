import streamlit as st

# Application Title
st.title("Ultimate Unit Converter App🌟")
st.markdown("""
### Convert Units in Real Time
Welcome to the **Ultimate Unit Converter App**! Effortlessly convert between various units for **Weight**, **Length**, **Time**, and more.
""")
st.sidebar.title("Navigation")
st.sidebar.markdown("🔧 Choose your preferences and start converting!")

# User Input: Select Conversion Category
category = st.selectbox(
    "💡 Choose a Conversion Category:",
    ["Length", "Weight", "Time", "Speed"]
)

#making functions
def convert_length(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Miles": 1609.34}
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_time(value, from_unit, to_unit):
    time_units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400}
    return value * time_units[from_unit] / time_units[to_unit]


def convert_speed(value, from_unit, to_unit):
    speed_units = {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694}
    return value * speed_units[from_unit] / speed_units[to_unit]

    # Display Relevant Conversion Inputs
if category == "Length":
    st.subheader("Length Conversion")
    value = st.number_input("Enter a value:", min_value=0.0)
    from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Centimeters", "Miles"])
    to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Centimeters", "Miles"])
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    st.subheader("Weight Conversion ")
    value = st.number_input("Enter a value:", min_value=0.0)
    from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Time":
    st.subheader("Time Conversion ")
    value = st.number_input("Enter a value:", min_value=0.0)
    from_unit = st.selectbox("From:", ["Seconds", "Minutes", "Hours", "Days"])
    to_unit = st.selectbox("To:", ["Seconds", "Minutes", "Hours", "Days"])
    if st.button("Convert"):
        result = convert_time(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")


elif category == "Speed":
    st.subheader("Speed Conversion")
    value = st.number_input("Enter a value:", min_value=0.0)
    from_unit = st.selectbox("From:", ["Meters per second", "Kilometers per hour", "Miles per hour"])
    to_unit = st.selectbox("To:", ["Meters per second", "Kilometers per hour", "Miles per hour"])
    if st.button("Convert"):
        result = convert_speed(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

st.markdown("**💻Created with love using Streamlit!**")