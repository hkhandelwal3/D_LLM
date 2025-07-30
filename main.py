import streamlit as st

# Title
st.title("Attribute Submission Form")

# Input fields
attribute_name = st.text_input("Enter Attribute Name:")
industry_name = st.text_input("Enter Industry Name:")

# Dropdown for Criticality
criticality = st.selectbox("Select Criticality:", ["High", "Medium", "Low"])

# Display the result and create prompt
if st.button("Submit"):
    st.markdown("### ✅ Submitted Information")
    st.write("**Attribute Name:**", attribute_name)
    st.write("**Industry Name:**", industry_name)
    st.write("**Criticality:**", criticality)

    # Create the prompt variable
    llm_prompt = (
        f"Generate data governance artefacts (definition, glossary, data dictionary, DQ rules, Python code) "
        f"for attribute '{attribute_name}' in {industry_name} industry with {criticality.lower()} criticality, "
        "following DAMA/ISO standards and Great Expectations style."
    )

    st.write("### LLM Prompt:")
    st.code(llm_prompt)
    st.code(llm_prompt)
