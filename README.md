# 🛡️ Quantum Shield: Eavesdropping Detector

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://quantum-eavesdropping-detector-4itzyq6nweap7qtvzarvjx.streamlit.app/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Quantum Shield** is a high-fidelity security dashboard designed to monitor and detect unauthorized eavesdropping in **Quantum Key Distribution (QKD)** networks using the **BB84 Protocol**.

---

## 🚀 Live Demo
Check out the live dashboard here: [Quantum Shield Live](https://quantum-eavesdropping-detector-4itzyq6nweap7qtvzarvjx.streamlit.app/)

---

## ✨ Key Features
- **Real-time Telemetry:** Visualizes Quantum Bit Error Rate (QBER) and alerts users to anomalies.
- **Attack Simulation:** Toggle between "Clean" and "Attack" scenarios to see how intercept-resend attacks disturb the channel.
- **Glassmorphism UI:** A premium, dark-themed interface built for modern security operations centers (SOC).
- **Dual Mode:** Supports both a live FastAPI backend for real quantum simulations and a "Demo Mode" for zero-setup exploration.

---

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/) (Python-based Web Framework)
- **Styling:** Custom CSS with Glassmorphism and CSS Variables
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (High-performance API)
- **Protocol:** BB84 Quantum Key Distribution Simulation
- **Data Science:** NumPy & Scikit-learn for QBER analysis

---

## 🏗️ Architecture
1. **The Quantum Engine:** Simulates the exchange of photons between Alice and Bob.
2. **The Eavesdropper (Eve):** Optionally intercepts photons, causing inevitable disturbance (Heisenberg's Uncertainty Principle).
3. **The Detector:** The FastAPI backend calculates the QBER and predicts if an attack is present.
4. **The Dashboard:** The Streamlit UI provides the security verdict and recommended actions.

---

## 💻 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/adityaakhuntia/quantum-eavesdropping-detector.git
cd quantum-eavesdropping-detector
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Backend (Optional for Live Data)
```bash
python -m uvicorn backend.api:app --reload
```

### 4. Launch the Dashboard
```bash
streamlit run dashboard/app.py
```

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 🤝 Connect
**Aditya Akhuntia**
- [GitHub](https://github.com/adityaakhuntia)
- [LinkedIn](https://linkedin.com/in/adityaakhuntia)
