import streamlit as st

# Title
st.title("Attribute Submission Form")

# Input fields
attribute_name = st.text_input("Enter Attribute Name:")
industry_name = st.text_input("Enter Industry Name:")

# Dropdown for Criticality
criticality = st.selectbox("Select Criticality:", ["High", "Medium", "Low"])

# Display the result
if st.button("Submit"):
    st.markdown("### ✅ Submitted Information")
    st.write("**Attribute Name:**", attribute_name)
    st.write("**Industry Name:**", industry_name)
    st.write("**Criticality:**", criticality)
 