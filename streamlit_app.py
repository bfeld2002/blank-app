import streamlit as st
import numpy as np
import pandas as pd

st.title("Feature Input App")

st.write("Adjust the sliders for each of the 10 features:")

# Sliders for 10 feature inputs
with st.form("input_form"):
    inputs = []
    for i in range(1, 11):
        value = st.slider(f"Feature {i}", min_value=0, max_value=5, value=5, step=1)
        inputs.append(value)
    
    submitted = st.form_submit_button("Submit")

if submitted:
    # Convert to DataFrame for display
    input_array = np.array(inputs).reshape(1, -1)
    df_input = pd.DataFrame(input_array, columns=[f"feature_{i}" for i in range(1, 11)])
    
    st.subheader("Your Input Values")
    st.write(df_input)
    

