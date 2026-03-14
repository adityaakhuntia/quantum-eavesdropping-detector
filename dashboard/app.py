import streamlit as st
import requests

st.title("🔐 Quantum Eavesdropping Detection")

attack = st.checkbox("Simulate Eavesdropping Attack")

if st.button("Run Detection"):
    response = requests.get(
        "http://127.0.0.1:8000/analyze",
        params={"eavesdrop": attack}
    )

    data = response.json()

    st.metric("Quantum Bit Error Rate (QBER)", data["qber"])
    
    if data["attack_detected"]:
        st.error("🚨 EAVESDROPPING DETECTED")
    else:
        st.success("✅ SECURE QUANTUM CHANNEL")
