import streamlit as st
import pandas as pd
import joblib

# ====================================================
# Page Configuration
# ====================================================

st.set_page_config(
    page_title="Predictive Maintenance System",
    page_icon="⚙️",
    layout="centered"
)

# ====================================================
# Load Saved Model and Label Encoder
# ====================================================

model = joblib.load("models/best_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

# ====================================================
# App Title
# ====================================================

st.title("⚙️ Predictive Maintenance Prediction System")

st.write("""
This application predicts whether a machine is likely to experience
failure based on operational sensor data using a Random Forest
Machine Learning model.
""")

st.markdown("---")

# ====================================================
# User Inputs
# ====================================================

st.header("Enter Machine Details")

machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature (K)",
    min_value=250.0,
    max_value=350.0,
    value=300.0,
    step=0.1
)

process_temp = st.number_input(
    "Process Temperature (K)",
    min_value=250.0,
    max_value=400.0,
    value=310.0,
    step=0.1
)

rpm = st.number_input(
    "Rotational Speed (RPM)",
    min_value=0,
    max_value=5000,
    value=1500,
    step=10
)

torque = st.number_input(
    "Torque (Nm)",
    min_value=0.0,
    max_value=100.0,
    value=40.0,
    step=0.1
)

tool_wear = st.number_input(
    "Tool Wear (Minutes)",
    min_value=0,
    max_value=300,
    value=20,
    step=1
)

st.markdown("---")

# ====================================================
# Prediction
# ====================================================

if st.button("Predict Machine Failure"):

    # Encode Machine Type
    machine_type_encoded = label_encoder.transform([machine_type])[0]

    # Create Input DataFrame
    input_data = pd.DataFrame({
        "Type": [machine_type_encoded],
        "Air temperature [K]": [air_temp],
        "Process temperature [K]": [process_temp],
        "Rotational speed [rpm]": [rpm],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear]
    })

    # Predict
    prediction = model.predict(input_data)[0]

    # Prediction Probability
    try:
        probability = model.predict_proba(input_data)
        confidence = probability.max() * 100
    except:
        confidence = None

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Machine Failure Predicted")
        st.write(
            "The model predicts that the machine is likely to fail. "
            "Preventive maintenance is recommended."
        )
    else:
        st.success("✅ Machine is NOT Likely to Fail")
        st.write(
            "The model predicts that the machine is operating normally."
        )

    if confidence is not None:
        st.metric("Prediction Confidence", f"{confidence:.2f}%")

    st.markdown("---")

    st.subheader("Input Summary")

    st.dataframe(input_data)

# ====================================================
# Footer
# ====================================================

st.markdown("---")

st.caption("Predictive Maintenance using Machine Learning")

st.caption("Model: Random Forest Classifier")