import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Streamlit app title
st.title("Algebraic Function and Derivative Plotter")

# User input for algebraic function
st.subheader("Enter an Algebraic Function")
user_input = st.text_input("Function (in terms of x):", value="x**2 + 3*x + 2")

# Sympy symbols and function parsing
x = sp.symbols('x')
try:
    function = sp.sympify(user_input)
    derivative = sp.diff(function, x)

    # Convert to numerical functions
    func = sp.lambdify(x, function, 'numpy')
    der_func = sp.lambdify(x, derivative, 'numpy')

    # Plot range
    x_range = st.slider("Select x range:", -10, 10, (-10, 10))

    # Generate plot
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = func(x_vals)
    y_der_vals = der_func(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="Function")
    plt.plot(x_vals, y_der_vals, label="Derivative", linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Function: {sp.pretty(function)} and its Derivative')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

except Exception as e:
    st.error(f"Error in function input: {e}")
