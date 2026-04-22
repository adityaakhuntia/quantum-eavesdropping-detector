# 🔐 Quantum Eavesdropping Detector

> **Runner-up — Quantathon 3.0, SRM University 2026**

An ML-powered system that detects eavesdropping attacks in BB84 Quantum Key Distribution (QKD) protocols with **90%+ detection accuracy** on simulated quantum channels.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## 🧠 What Is This?

In quantum cryptography, BB84 is the gold-standard protocol for generating secure encryption keys. The problem: an eavesdropper (Eve) intercepting the quantum channel introduces measurable statistical anomalies — a spike in the **Quantum Bit Error Rate (QBER)**.

This system:
1. **Simulates** a complete BB84 QKD channel with Alice, Bob, and an optional Eve
2. **Detects** eavesdropping attacks using a trained ML anomaly detection model
3. **Visualizes** real-time threat levels and attack classifications on a live Streamlit dashboard

---

## ✨ Key Features

- 🔬 **BB84 Protocol Simulation** — full quantum channel simulation with configurable eavesdropping intensity
- 🤖 **ML Anomaly Detection** — Scikit-learn classifier trained on QBER patterns to flag attacks
- 📊 **Real-Time Dashboard** — Streamlit UI with live threat visualization and attack classification feed
- ⚡ **FastAPI Backend** — RESTful API serving detection results with low latency
- 🎯 **90%+ Detection Accuracy** — validated on simulated quantum channel datasets

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│              Streamlit Dashboard             │
│         (Live Threat Visualization)          │
└─────────────────┬───────────────────────────┘
                  │ HTTP
┌─────────────────▼───────────────────────────┐
│              FastAPI Backend                 │
│         (REST API · Detection Engine)        │
└─────────────────┬───────────────────────────┘
                  │
       ┌──────────┴──────────┐
       ▼                     ▼
┌──────────────┐    ┌────────────────┐
│  ML Model    │    │  Quantum Sim   │
│ (Scikit-learn│    │ (BB84 Protocol)│
│  Classifier) │    │ Alice/Bob/Eve  │
└──────────────┘    └────────────────┘
```

---

## 📁 Project Structure

```
quantum-eavesdropping-detector/
│
├── backend/          # FastAPI application & REST endpoints
├── ml_model/         # Model training & inference (train.py)
├── quantum_sim/      # BB84 protocol simulation logic
├── dashboard/        # Streamlit frontend (app.py)
├── features/         # Feature engineering & QBER extraction
├── data/             # Simulated quantum channel datasets
│
├── requirements.txt  # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/adityaakhuntia/quantum-eavesdropping-detector.git
cd quantum-eavesdropping-detector

# Install dependencies
pip install -r requirements.txt
```

### Running the System

```bash
# Step 1: Train the ML model
python ml_model/train.py

# Step 2: Start the FastAPI backend
uvicorn backend.api:app --reload

# Step 3: Launch the Streamlit dashboard
streamlit run dashboard/app.py
```

Then open `http://localhost:8501` to view the live dashboard.

---

## 📈 Results

| Metric | Value |
|---|---|
| Detection Accuracy | **90%+** |
| Protocol Simulated | BB84 QKD |
| Attack Types Detected | Intercept-Resend, Man-in-the-Middle |
| Backend Latency | < 100ms per request |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Quantum Simulation | Python (custom BB84 implementation) |
| ML Model | Scikit-learn (anomaly classification) |
| Feature Engineering | NumPy, Pandas (QBER statistical features) |
| Backend API | FastAPI + Uvicorn |
| Frontend Dashboard | Streamlit |

---

## 🏆 Competition

Built for and presented at **Quantathon 3.0** — a university-wide ML & quantum computing competition at SRM Institute of Science and Technology. The team secured **2nd place** across all competing teams.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
Made by <a href="https://github.com/adityaakhuntia">Aditya Khuntia</a> · 
<a href="https://linkedin.com/in/adityakhuntia">LinkedIn</a>
</div>
