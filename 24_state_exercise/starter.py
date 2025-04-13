import streamlit as st

st.title("Exercise: State Management")

st.subheader("Temperature conversion")

# Initialize state with temperatures.
# Use the freezing point of water

# Write a callback to convert the temperature in Celsius
# to Farenheit and Kelvin. Change the values in the state
# appropriately

# Same thing, but converting from Farenheit to Celsius
# and Kelvin

# Same thing, but converting from Kelvin to Celsius
# and Farenheint

# Write a callback that adds whatever number the user
# inputs to the Celsius box. Use args.

# Write a callback to sets the temperatures depending on
# which button the user clicks. Use kwargs.

if "celsius" not in st.session_state:
    st.session_state["celsius"] = 0.00

if "fahrenheit" not in st.session_state:
    st.session_state["fahrenheit"] = 32.00

if "kelvin" not in st.session_state:
    st.session_state["kelvin"] = 273.15

def convert(deg_type: str):
    cel = st.session_state["celsius"]
    fah = st.session_state["fahrenheit"]
    kel = st.session_state["kelvin"]

    if deg_type == "c":
        st.session_state["fahrenheit"] = (cel * 9/5) + 32
        st.session_state["kelvin"] = cel + 273.15
    elif deg_type == "f":
        st.session_state["celsius"] = (fah - 32) * 5/9
        st.session_state["kelvin"] = ((fah - 32) * 5/9) + 273.15
    elif deg_type == "k":
        st.session_state["celsius"] = kel - 273.15
        st.session_state["fahrenheit"] = ((kel - 273.15) * 9/5) + 32
    else:
        pass

def celsius_add(_num):
    st.session_state['celsius'] += _num
    convert('c')

def set_temperatures(celsius, fahrenheit, kelvin):
    st.session_state['celsius'] = celsius
    st.session_state['fahrenheit'] = fahrenheit
    st.session_state['kelvin'] = kelvin

col1, col2, col3 = st.columns(3)

# Hook up the first 3 callbacks to the input widgets
col1.number_input("Celsius",
    step=0.01,
    key="celsius",
    on_change=convert,
    args=('c')
)
col2.number_input("Fahrenheit",
    step=0.01,
    key="fahrenheit",
    on_change=convert,
    args=('f')
)
col3.number_input("Kelvin",
    step=0.01,
    key="kelvin",
    on_change=convert,
    args=("k")
)

# Hook up the 4th callback to the button. Use args.
col1, _, _ = st.columns(3)
num = col1.number_input("Add to Celsius", step=1)
col1.button("Add", type="primary", on_click=celsius_add, args=(num,))

col1, col2, col3 = st.columns(3)

# Hook up the last callback to each button. Use kwargs.
col1.button('🧊 Freezing point of water', 
            on_click=set_temperatures, 
            kwargs=dict(celsius=0.00, fahrenheit=32.00, kelvin=273.15))
col2.button('🔥 Boiling point of water',
            on_click=set_temperatures,
            kwargs=dict(celsius=100.00, fahrenheit=212.00, kelvin=373.15))
col3.button('🥶 Absolute zero',
            on_click=set_temperatures,
            kwargs=dict(celsius=-273.15, fahrenheit=-459.67, kelvin=0.00))

st.write(st.session_state)