# calculator_app.py

import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Select the operation
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Perform the selected operation
def calculate(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."

# Button to trigger calculation
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"Result: {result}")
