from datetime import datetime
import time

import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/analyze"
DEFAULT_THRESHOLD = 0.25


st.set_page_config(
    page_title="Quantum Shield | Eavesdropping Detector",
    page_icon="Q",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def inject_styles():
    st.markdown(
        """
        <style>
            :root {
                --bg: #020406;
                --panel: rgba(14, 18, 22, 0.76);
                --panel-strong: rgba(22, 27, 33, 0.92);
                --ink: #f8fafc;
                --muted: #a7b0bc;
                --soft: #d9e2ec;
                --line: rgba(226, 232, 240, 0.16);
                --blue: #4ba3db;
                --blue-strong: #6ec7ff;
                --green: #6adf7c;
                --amber: #ffd166;
                --red: #ff5c7a;
                --shadow: 0 24px 80px rgba(0, 0, 0, 0.42);
            }

            .stApp {
                background:
                    radial-gradient(circle at 14% 42%, rgba(75, 163, 219, 0.42), transparent 31%),
                    radial-gradient(circle at 78% 18%, rgba(255, 255, 255, 0.10), transparent 25%),
                    linear-gradient(135deg, #000000 0%, #06090d 42%, #101010 100%);
                color: var(--ink);
            }

            .block-container {
                max-width: 1180px;
                padding-top: 1.1rem;
                padding-bottom: 2.5rem;
            }

            header[data-testid="stHeader"] {
                background: transparent;
            }

            div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0;
                position: fixed;
            }

            .browser-frame {
                overflow: hidden;
                border: 1px solid rgba(255, 255, 255, 0.18);
                border-radius: 8px;
                background: rgba(0, 0, 0, 0.48);
                box-shadow: var(--shadow);
                animation: liftIn 520ms ease-out both;
            }

            .browser-top {
                display: grid;
                grid-template-columns: auto 1fr auto;
                gap: 18px;
                align-items: center;
                padding: 10px 14px;
                background: #c7cbd0;
            }

            .traffic {
                display: flex;
                gap: 12px;
            }

            .traffic span {
                width: 18px;
                height: 18px;
                border-radius: 50%;
                display: block;
            }

            .traffic span:nth-child(1) { background: #ff5f6d; }
            .traffic span:nth-child(2) { background: #ffd166; }
            .traffic span:nth-child(3) { background: #5bd23c; }

            .url-bar {
                height: 16px;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.78);
                box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.42);
            }

            .window-actions {
                display: flex;
                gap: 16px;
            }

            .window-actions span {
                width: 44px;
                height: 19px;
                border-radius: 5px;
                background: rgba(255, 255, 255, 0.68);
                display: block;
            }

            .hero {
                position: relative;
                overflow: hidden;
                min-height: 410px;
                padding: 54px 62px 42px;
                background:
                    linear-gradient(104deg, rgba(0, 0, 0, 0.92) 0%, rgba(4, 8, 11, 0.9) 42%, rgba(38, 38, 38, 0.86) 100%),
                    radial-gradient(circle at 12% 72%, rgba(75, 163, 219, 0.64), transparent 35%);
            }

            .hero:before {
                content: "";
                position: absolute;
                inset: 0;
                background:
                    linear-gradient(90deg, rgba(75, 163, 219, 0.08) 1px, transparent 1px),
                    linear-gradient(rgba(255, 255, 255, 0.035) 1px, transparent 1px);
                background-size: 58px 58px;
                mask-image: linear-gradient(90deg, rgba(0, 0, 0, 0.9), transparent 78%);
                pointer-events: none;
            }

            .hero:after {
                content: "";
                position: absolute;
                inset: 0;
                background: linear-gradient(112deg, transparent 12%, rgba(255, 255, 255, 0.18) 45%, transparent 72%);
                transform: translateX(-120%);
                animation: scan 6s ease-in-out infinite;
                pointer-events: none;
            }

            .hero-inner {
                position: relative;
                z-index: 1;
                display: grid;
                grid-template-columns: minmax(0, 0.98fr) minmax(330px, 0.72fr);
                gap: 56px;
                align-items: center;
            }

            .eyebrow {
                display: inline-flex;
                align-items: center;
                gap: 9px;
                padding: 8px 12px;
                border: 1px solid rgba(110, 199, 255, 0.28);
                border-radius: 999px;
                color: var(--blue-strong);
                background: rgba(255, 255, 255, 0.045);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                backdrop-filter: blur(14px);
            }

            .pulse-dot {
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: var(--green);
                box-shadow: 0 0 0 rgba(106, 223, 124, 0.54);
                animation: pulse 1.7s infinite;
            }

            .hero h1 {
                margin: 22px 0 16px;
                max-width: 660px;
                color: #ffffff;
                font-size: clamp(2.65rem, 5.4vw, 5.8rem);
                line-height: 0.92;
                letter-spacing: 0;
                text-wrap: balance;
            }

            .hero-copy {
                max-width: 660px;
                margin: 0;
                color: var(--soft);
                font-size: 1.04rem;
                line-height: 1.75;
            }

            .hero-actions {
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                margin-top: 24px;
            }

            .hero-pill {
                border: 1px solid rgba(255, 255, 255, 0.16);
                border-radius: 999px;
                padding: 9px 12px;
                color: var(--soft);
                background: rgba(255, 255, 255, 0.055);
                font-size: 0.86rem;
                font-weight: 700;
                backdrop-filter: blur(12px);
            }

            .feature-glass {
                position: relative;
                overflow: hidden;
                min-height: 330px;
                border: 2px solid rgba(245, 248, 255, 0.84);
                border-right-color: rgba(245, 248, 255, 0.22);
                border-bottom-color: rgba(245, 248, 255, 0.28);
                border-radius: 44px 8px 8px 8px;
                padding: 32px 30px;
                background:
                    linear-gradient(135deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.10)),
                    radial-gradient(circle at 0% 88%, rgba(75, 163, 219, 0.42), transparent 50%);
                box-shadow: 0 18px 70px rgba(0, 0, 0, 0.36);
                backdrop-filter: blur(16px);
            }

            .feature-glass:before {
                content: "";
                position: absolute;
                inset: 0;
                background: linear-gradient(115deg, transparent, rgba(255, 255, 255, 0.16), transparent);
                transform: translateX(-120%);
                animation: glassSweep 5s ease-in-out infinite;
            }

            .feature-item {
                position: relative;
                z-index: 1;
                display: grid;
                grid-template-columns: 48px 1fr;
                gap: 16px;
                align-items: start;
                margin-bottom: 26px;
            }

            .feature-item:last-child {
                margin-bottom: 0;
            }

            .line-icon {
                width: 42px;
                height: 42px;
                border: 2px solid rgba(255, 255, 255, 0.86);
                border-radius: 50%;
                position: relative;
            }

            .line-icon.user:after {
                content: "";
                position: absolute;
                left: 10px;
                right: 10px;
                bottom: 8px;
                height: 14px;
                border: 2px solid rgba(255, 255, 255, 0.86);
                border-radius: 50% 50% 44% 44%;
            }

            .line-icon.user:before {
                content: "";
                position: absolute;
                left: 13px;
                top: 7px;
                width: 12px;
                height: 12px;
                border: 2px solid rgba(255, 255, 255, 0.86);
                border-radius: 50%;
            }

            .line-icon.signal:before,
            .line-icon.signal:after {
                content: "";
                position: absolute;
                inset: 10px;
                border: 2px solid rgba(255, 255, 255, 0.86);
                border-radius: 6px;
                transform: rotate(45deg);
            }

            .line-icon.signal:after {
                inset: 16px;
                background: rgba(255, 255, 255, 0.86);
            }

            .line-icon.shield {
                border-radius: 12px 12px 18px 18px;
                transform: rotate(45deg);
            }

            .line-icon.shield:after {
                content: "";
                position: absolute;
                left: 12px;
                top: 7px;
                width: 10px;
                height: 18px;
                border-right: 2px solid rgba(255, 255, 255, 0.86);
                border-bottom: 2px solid rgba(255, 255, 255, 0.86);
                transform: rotate(0deg);
            }

            .feature-title {
                margin: 0 0 8px;
                color: #ffffff;
                font-size: 1.25rem;
                font-weight: 750;
            }

            .feature-copy {
                margin: 0;
                color: rgba(248, 250, 252, 0.78);
                font-size: 0.93rem;
                line-height: 1.55;
            }

            .insight-strip {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 12px;
                margin: 16px 0 18px;
            }

            .mini-stat {
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 14px;
                background: rgba(255, 255, 255, 0.055);
                backdrop-filter: blur(12px);
            }

            .mini-label {
                color: var(--muted);
                font-size: 0.72rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .mini-value {
                margin-top: 6px;
                color: #ffffff;
                font-size: 1.4rem;
                font-weight: 850;
            }

            .mini-note {
                margin-top: 4px;
                color: var(--muted);
                font-size: 0.82rem;
            }

            .section-title {
                margin: 0 0 8px;
                color: #ffffff;
                font-size: 1.08rem;
                font-weight: 850;
            }

            .section-copy {
                margin: 0 0 18px;
                color: var(--muted);
                line-height: 1.55;
                font-size: 0.94rem;
            }

            .panel {
                border: 1px solid var(--line);
                border-radius: 8px;
                background: var(--panel);
                box-shadow: 0 18px 54px rgba(0, 0, 0, 0.28);
                padding: 22px;
                min-height: 100%;
                backdrop-filter: blur(18px);
                animation: liftIn 600ms ease-out both;
            }

            .detail-grid {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 12px;
                margin-top: 16px;
            }

            .detail-card {
                border: 1px solid var(--line);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.055);
                padding: 16px;
                min-height: 118px;
                transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease, background 180ms ease;
            }

            .detail-card:hover {
                transform: translateY(-3px);
                border-color: rgba(110, 199, 255, 0.42);
                background: rgba(255, 255, 255, 0.08);
                box-shadow: 0 16px 36px rgba(75, 163, 219, 0.16);
            }

            .detail-label {
                color: var(--muted);
                font-size: 0.74rem;
                font-weight: 850;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }

            .detail-value {
                margin-top: 8px;
                color: #ffffff;
                font-size: 1.48rem;
                font-weight: 850;
            }

            .detail-note {
                margin-top: 6px;
                color: var(--muted);
                font-size: 0.84rem;
                line-height: 1.45;
            }

            .status-banner {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 16px;
                border-radius: 8px;
                padding: 18px 20px;
                margin-top: 16px;
                border: 1px solid transparent;
                animation: liftIn 420ms ease-out both;
            }

            .status-safe {
                color: #d8ffe0;
                border-color: rgba(106, 223, 124, 0.34);
                background: linear-gradient(135deg, rgba(24, 108, 44, 0.52), rgba(19, 35, 24, 0.8));
            }

            .status-alert {
                color: #ffe6eb;
                border-color: rgba(255, 92, 122, 0.4);
                background: linear-gradient(135deg, rgba(155, 22, 53, 0.58), rgba(38, 15, 22, 0.86));
            }

            .status-watch {
                color: #fff6d7;
                border-color: rgba(255, 209, 102, 0.38);
                background: linear-gradient(135deg, rgba(132, 91, 21, 0.56), rgba(35, 26, 13, 0.84));
            }

            .status-title {
                margin: 0;
                color: inherit;
                font-size: 1.08rem;
                font-weight: 850;
            }

            .status-copy {
                margin: 4px 0 0;
                color: inherit;
                font-size: 0.92rem;
                opacity: 0.82;
            }

            .status-pill {
                flex: 0 0 auto;
                border-radius: 999px;
                padding: 8px 12px;
                background: rgba(255, 255, 255, 0.12);
                color: inherit;
                font-size: 0.78rem;
                font-weight: 850;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }

            .step-list {
                display: grid;
                gap: 10px;
                margin-top: 4px;
            }

            .step {
                display: grid;
                grid-template-columns: 34px 1fr;
                gap: 12px;
                align-items: start;
                padding: 12px;
                border: 1px solid var(--line);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.045);
            }

            .step-num {
                display: grid;
                place-items: center;
                width: 34px;
                height: 34px;
                border-radius: 8px;
                color: #ffffff;
                background: linear-gradient(135deg, rgba(75, 163, 219, 0.82), rgba(75, 163, 219, 0.24));
                font-weight: 850;
            }

            .step strong {
                display: block;
                color: #ffffff;
                font-size: 0.94rem;
            }

            .step span {
                display: block;
                margin-top: 2px;
                color: var(--muted);
                font-size: 0.84rem;
                line-height: 1.42;
            }

            .stMarkdown,
            .stCaption,
            .stText,
            label,
            p,
            span {
                color: var(--soft);
            }

            div[data-testid="stVerticalBlockBorderWrapper"] {
                border-color: var(--line);
                border-radius: 8px;
                background: var(--panel);
                box-shadow: 0 18px 54px rgba(0, 0, 0, 0.28);
                backdrop-filter: blur(18px);
                animation: liftIn 600ms ease-out both;
            }

            div[data-testid="stMetric"] {
                border: 1px solid var(--line);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.055);
                padding: 15px 16px;
                box-shadow: 0 12px 32px rgba(0, 0, 0, 0.18);
            }

            div[data-testid="stMetric"] label,
            div[data-testid="stMetric"] [data-testid="stMetricValue"] {
                color: #ffffff;
            }

            div.stButton > button {
                width: 100%;
                min-height: 50px;
                border: 1px solid rgba(110, 199, 255, 0.46);
                border-radius: 8px;
                color: #ffffff;
                background: linear-gradient(135deg, #2b8ac1, #145a82 48%, #111827);
                box-shadow: 0 16px 34px rgba(75, 163, 219, 0.28);
                font-weight: 850;
                transition: transform 160ms ease, box-shadow 160ms ease, filter 160ms ease;
            }

            div.stButton > button:hover {
                color: #ffffff;
                transform: translateY(-2px);
                filter: brightness(1.08);
                box-shadow: 0 20px 42px rgba(75, 163, 219, 0.36);
            }

            div.stButton > button:active {
                transform: translateY(0);
            }

            .stProgress > div > div > div > div {
                background: linear-gradient(90deg, var(--green), var(--amber), var(--red));
            }

            .stDataFrame {
                border: 1px solid var(--line);
                border-radius: 8px;
                overflow: hidden;
            }

            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(106, 223, 124, 0.54); }
                70% { box-shadow: 0 0 0 11px rgba(106, 223, 124, 0); }
                100% { box-shadow: 0 0 0 0 rgba(106, 223, 124, 0); }
            }

            @keyframes scan {
                0%, 56% { transform: translateX(-120%); }
                82%, 100% { transform: translateX(120%); }
            }

            @keyframes glassSweep {
                0%, 48% { transform: translateX(-120%); }
                74%, 100% { transform: translateX(120%); }
            }

            @keyframes liftIn {
                from { opacity: 0; transform: translateY(14px); }
                to { opacity: 1; transform: translateY(0); }
            }

            @media (max-width: 900px) {
                .browser-top {
                    grid-template-columns: auto 1fr;
                }

                .window-actions {
                    display: none;
                }

                .hero {
                    padding: 34px 22px;
                }

                .hero-inner {
                    grid-template-columns: 1fr;
                    gap: 28px;
                }

                .feature-glass {
                    border-radius: 28px 8px 8px 8px;
                    min-height: auto;
                }

                .insight-strip,
                .detail-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def qber_band(qber, threshold=DEFAULT_THRESHOLD):
    watch_threshold = max(0.06, threshold * 0.5)
    if qber >= threshold:
        return "Critical", "High disturbance across the sifted key.", "alert"
    if qber >= watch_threshold:
        return "Watch", "Noise is elevated and deserves another scan.", "watch"
    return "Clean", "Channel noise is within a healthy operating range.", "safe"


def security_score(qber):
    return max(0, min(100, round((1 - qber) * 100)))


def confidence_level(qber, attack_detected):
    if attack_detected:
        return min(99, 72 + round(qber * 70))
    return max(62, 96 - round(qber * 85))


def render_hero():
    st.markdown(
        """
        <section class="browser-frame">
            <div class="browser-top">
                <div class="traffic"><span></span><span></span><span></span></div>
                <div class="url-bar"></div>
                <div class="window-actions"><span></span><span></span></div>
            </div>
            <div class="hero">
                <div class="hero-inner">
                    <div>
                        <div class="eyebrow"><span class="pulse-dot"></span> Live BB84 security monitor</div>
                        <h1>Quantum Shield Detection</h1>
                        <p class="hero-copy">
                            A modern command center for spotting eavesdropping in quantum key distribution.
                            Simulate the BB84 channel, measure QBER, and turn raw model output into a clear
                            security decision.
                        </p>
                        <div class="hero-actions">
                            <span class="hero-pill">Dark glass UI</span>
                            <span class="hero-pill">Animated analysis</span>
                            <span class="hero-pill">Scan history</span>
                        </div>
                    </div>
                    <div class="feature-glass">
                        <div class="feature-item">
                            <div class="line-icon user"></div>
                            <div>
                                <p class="feature-title">User-friendly controls</p>
                                <p class="feature-copy">Run clean or attack scenarios with a focused, simple scan panel.</p>
                            </div>
                        </div>
                        <div class="feature-item">
                            <div class="line-icon signal"></div>
                            <div>
                                <p class="feature-title">Seamless integration</p>
                                <p class="feature-copy">FastAPI analysis plugs directly into the Streamlit dashboard.</p>
                            </div>
                        </div>
                        <div class="feature-item">
                            <div class="line-icon shield"></div>
                            <div>
                                <p class="feature-title">Security insight</p>
                                <p class="feature-copy">QBER bands, verdicts, confidence, and action hints in one view.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_insight_strip(scan_count):
    st.markdown(
        f"""
        <div class="insight-strip">
            <div class="mini-stat">
                <div class="mini-label">Protocol</div>
                <div class="mini-value">BB84</div>
                <div class="mini-note">Quantum key exchange</div>
            </div>
            <div class="mini-stat">
                <div class="mini-label">Analyzer</div>
                <div class="mini-value">ML</div>
                <div class="mini-note">Feature-based detector</div>
            </div>
            <div class="mini-stat">
                <div class="mini-label">Signal</div>
                <div class="mini-value">QBER</div>
                <div class="mini-note">Error-rate telemetry</div>
            </div>
            <div class="mini-stat">
                <div class="mini-label">Scans</div>
                <div class="mini-value">{scan_count}</div>
                <div class="mini-note">Stored this session</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_details(qber, attack_detected, threshold, mode):
    band, note, tone = qber_band(qber, threshold)
    score = security_score(qber)
    confidence = confidence_level(qber, attack_detected)
    status_class = "status-alert" if attack_detected else ("status-watch" if tone == "watch" else "status-safe")
    status_title = "Eavesdropping detected" if attack_detected else ("Noise requires attention" if tone == "watch" else "Secure quantum channel")
    status_copy = (
        "The classifier found a disturbance pattern consistent with an active intercept-resend attack."
        if attack_detected
        else "The measured error rate and classifier output currently support a protected BB84 exchange."
    )
    status_pill = "Alert" if attack_detected else ("Watch" if tone == "watch" else "Protected")

    st.markdown(
        f"""
        <div class="status-banner {status_class}">
            <div>
                <p class="status-title">{status_title}</p>
                <p class="status-copy">{status_copy}</p>
            </div>
            <div class="status-pill">{status_pill}</div>
        </div>
        <div class="detail-grid">
            <div class="detail-card">
                <div class="detail-label">Security score</div>
                <div class="detail-value">{score}%</div>
                <div class="detail-note">Higher means lower measured disturbance.</div>
            </div>
            <div class="detail-card">
                <div class="detail-label">QBER band</div>
                <div class="detail-value">{band}</div>
                <div class="detail-note">{note}</div>
            </div>
            <div class="detail-card">
                <div class="detail-label">Confidence</div>
                <div class="detail-value">{confidence}%</div>
                <div class="detail-note">Dashboard confidence based on verdict and QBER strength.</div>
            </div>
        </div>
        <div class="detail-grid">
            <div class="detail-card">
                <div class="detail-label">Scan mode</div>
                <div class="detail-value">{mode}</div>
                <div class="detail-note">Selected review depth for this run.</div>
            </div>
            <div class="detail-card">
                <div class="detail-label">Threshold</div>
                <div class="detail-value">{threshold:.0%}</div>
                <div class="detail-note">Local QBER threshold used for dashboard risk bands.</div>
            </div>
            <div class="detail-card">
                <div class="detail-label">Model decision</div>
                <div class="detail-value">{status_pill}</div>
                <div class="detail-note">Machine-learning verdict returned by the backend.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(min(1.0, qber), text=f"QBER intensity: {qber:.2%}")

    if attack_detected:
        st.error("Recommended action: pause key acceptance, rotate the channel, and run a clean baseline scan.")
    elif tone == "watch":
        st.warning("Recommended action: run another sample and compare against the previous QBER trend.")
    else:
        st.success("Recommended action: continue monitoring and keep the current baseline.")


def render_workflow():
    st.markdown(
        """
        <div class="panel">
            <p class="section-title">Detection pipeline</p>
            <p class="section-copy">The dashboard turns the backend response into a security workflow.</p>
            <div class="step-list">
                <div class="step">
                    <div class="step-num">1</div>
                    <div><strong>BB84 simulation</strong><span>Alice and Bob exchange randomized bits and bases.</span></div>
                </div>
                <div class="step">
                    <div class="step-num">2</div>
                    <div><strong>Attack option</strong><span>The eavesdropper toggle adds disturbance to the channel.</span></div>
                </div>
                <div class="step">
                    <div class="step-num">3</div>
                    <div><strong>QBER telemetry</strong><span>The API calculates bit mismatches and prepares model features.</span></div>
                </div>
                <div class="step">
                    <div class="step-num">4</div>
                    <div><strong>Security verdict</strong><span>The dashboard explains the model output with risk bands and actions.</span></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def add_history_row(qber, attack, attack_detected, mode):
    st.session_state.scan_history.insert(
        0,
        {
            "time": datetime.now().strftime("%H:%M:%S"),
            "mode": mode,
            "scenario": "Attack" if attack else "Clean",
            "qber": f"{qber:.2%}",
            "decision": "Alert" if attack_detected else "Secure",
            "score": f"{security_score(qber)}%",
        },
    )
    st.session_state.scan_history = st.session_state.scan_history[:6]


if "scan_history" not in st.session_state:
    st.session_state.scan_history = []


inject_styles()
render_hero()
render_insight_strip(len(st.session_state.scan_history))

control_col, result_col = st.columns([0.37, 0.63], gap="large")

with control_col:
    with st.container(border=True):
        st.markdown(
            """
            <p class="section-title">Run a channel scan</p>
            <p class="section-copy">Tune the scenario, sensitivity, and analysis mode before sending it to the API.</p>
            """,
            unsafe_allow_html=True,
        )

        attack = st.toggle(
            "Simulate eavesdropping attack",
            value=False,
            help="Adds an intercept-resend style disturbance to the BB84 simulation.",
        )
        scan_mode = st.selectbox(
            "Scan mode",
            ["Quick", "Balanced", "Forensic"],
            index=1,
            help="Changes how the dashboard labels the scan depth. The API response remains the source of truth.",
        )
        threshold = st.slider(
            "Dashboard QBER alert threshold",
            min_value=0.10,
            max_value=0.40,
            value=DEFAULT_THRESHOLD,
            step=0.01,
            format="%.2f",
            help="Used for the dashboard risk band in addition to the backend model verdict.",
        )
        st.caption("Backend endpoint: http://127.0.0.1:8000/analyze")
        run_scan = st.button("Run detection", type="primary")

    render_workflow()

with result_col:
    with st.container(border=True):
        st.markdown(
            """
            <p class="section-title">Security result</p>
            <p class="section-copy">Live verdict, QBER intensity, confidence, and next action after each scan.</p>
            """,
            unsafe_allow_html=True,
        )

        if run_scan:
            with st.spinner("Analyzing photon disturbance pattern..."):
                time.sleep(0.35)
                try:
                    response = requests.get(API_URL, params={"eavesdrop": attack}, timeout=8)
                    response.raise_for_status()
                    data = response.json()
                except requests.RequestException as exc:
                    st.error("The analyzer API is not reachable. Start it with: python -m uvicorn backend.api:app --reload")
                    st.caption(f"Request detail: {exc}")
                else:
                    qber = float(data.get("qber", 0))
                    attack_detected = bool(data.get("attack_detected", False))
                    add_history_row(qber, attack, attack_detected, scan_mode)

                    metric_col_a, metric_col_b, metric_col_c = st.columns(3)
                    metric_col_a.metric("QBER", f"{qber:.2%}")
                    metric_col_b.metric("Scenario", "Attack" if attack else "Clean")
                    metric_col_c.metric("Decision", "Alert" if attack_detected else "Secure")

                    render_details(qber, attack_detected, threshold, scan_mode)
        else:
            st.info("Select a scenario, then run detection to generate a live security verdict.")
            st.markdown(
                """
                <div class="detail-grid">
                    <div class="detail-card">
                        <div class="detail-label">Feature</div>
                        <div class="detail-value">History</div>
                        <div class="detail-note">Recent scan rows appear after your first run.</div>
                    </div>
                    <div class="detail-card">
                        <div class="detail-label">Feature</div>
                        <div class="detail-value">Risk bands</div>
                        <div class="detail-note">The dashboard adds readable QBER bands to the model output.</div>
                    </div>
                    <div class="detail-card">
                        <div class="detail-label">Feature</div>
                        <div class="detail-value">Actions</div>
                        <div class="detail-note">Each verdict includes a practical next step.</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if st.session_state.scan_history:
        with st.container(border=True):
            st.markdown(
                """
                <p class="section-title">Recent scans</p>
                <p class="section-copy">Session history helps compare clean baselines and attack simulations.</p>
                """,
                unsafe_allow_html=True,
            )
            st.dataframe(st.session_state.scan_history, hide_index=True, use_container_width=True)
