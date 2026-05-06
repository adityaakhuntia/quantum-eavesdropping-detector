# 🛡️ Quantum Shield: Eavesdropping Detector  
### **An Advanced Quantum Security Monitoring Dashboard**
  
[![Live Demo](https://img.shields.io/badge/LIVE_DEMO-Visit_Website-success?style=for-the-badge&logo=streamlit)](https://quantum-eavesdropping-detector.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/SOURCE_CODE-View_on_GitHub-blue?style=for-the-badge&logo=github)](https://github.com/adityaakhuntia/quantum-eavesdropping-detector)

---

## 🌌 Project Overview
**Quantum Shield** is a high-performance security platform that leverages the principles of **Quantum Mechanics** to protect communication channels. This project simulates a **BB84 Quantum Key Distribution (QKD)** protocol and uses an intelligent detection engine to identify intercept-resend attacks (eavesdropping) in real-time.

> **"In the quantum world, observation is an intervention."** 
> This project demonstrates how we can detect hackers simply by the disturbance they leave on individual photons.
  
---

## 🎯 Key Highlights for Recruiters
*   **Full-Stack Integration:** Seamlessly connects a **FastAPI** backend with a high-fidelity **Streamlit** frontend.
*   **Premium UX/UI:** Implements a modern **Glassmorphism** design system with custom CSS for a state-of-the-art feel.
*   **Robust Logic:** Handles complex physics simulations (BB84 bases, photon polarization) and translates them into actionable security metrics.
*   **Deployment Ready:** Architected with a "Demo Mode" fallback to ensure 100% uptime for portfolio visitors.

---

## ✨ Core Features
| Feature | Description |
| :--- | :--- |
| **🔍 Real-time Detection** | Calculates QBER (Quantum Bit Error Rate) to detect Eve's presence. |
| **🛡️ Attack Simulation** | Live toggle to simulate Intercept-Resend attacks on the quantum channel. |
| **📊 Security Telemetry** | Dynamic risk bands and historical scan tracking for trend analysis. |
| **💠 Glassmorphism UI** | A sleek, dark-themed dashboard designed for Security Operation Centers (SOC). |
| **⚙️ Dual Operation** | Supports both local API-driven data and a standalone simulation mode. |

---

## 🛠️ Technical Implementation
### **The Stack**
- **Frontend:** Streamlit, Custom CSS, JavaScript (Animations)
- **Backend:** FastAPI, Uvicorn
- **Logic:** BB84 Protocol Simulation, NumPy, Python 3.11+
- **DevOps:** Git, GitHub Actions, Streamlit Cloud

### **The Architecture**
1.  **Quantum Simulation:** Alice and Bob exchange qubits using randomized bases.
2.  **Intercept-Resend:** If enabled, "Eve" intercepts the photons, causing a measurable 25% increase in error rates.
3.  **QBER Analysis:** The system compares shifted keys and flags any error rate above the security threshold (typically 11-15%).
4.  **Verdict Engine:** Translates raw physics data into "Alert" or "Secure" status for the user.

---

## 🚀 Getting Started

### **1. Clone & Install**
```bash
git clone https://github.com/adityaakhuntia/quantum-eavesdropping-detector.git
cd quantum-eavesdropping-detector
pip install -r requirements.txt
```

### **2. Launch Dashboard**
```bash
streamlit run dashboard/app.py
```
*(The app defaults to **Demo Mode** for an instant experience. To use the real API, start the FastAPI server in `backend/`)*

---
  
## 🤝 Connect & Collaborate
**Aditya Akhuntia**  
*Full-Stack Developer & Quantum Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/adityaakhuntia)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-lightgrey?style=flat-square&logo=github)](https://github.com/adityaakhuntia)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-orange?style=flat-square&logo=react)](https://adityaakhuntia.github.io)

---
*Developed as a showcase of secure communication protocols and modern web architecture.*
