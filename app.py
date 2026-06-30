import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MindScan | Mental Health Analysis",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg:        #0d0f14;
    --surface:   #13161e;
    --border:    #1f2433;
    --accent:    #c8a96e;
    --accent2:   #8b9fc4;
    --text:      #e8e4dc;
    --muted:     #6b7280;
    --danger:    #c46e6e;
    --safe:      #6ea88a;
    --warning:   #c4a06e;
    --info:      #6e8ec4;
    --stress:    #a06ec4;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stDecoration"] { display: none; }
[data-testid="stToolbar"] { display: none; }
footer { display: none; }

/* Hide streamlit branding */
#MainMenu { visibility: hidden; }

/* ── Header ── */
.header-wrap {
    text-align: center;
    padding: 3.5rem 0 2rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2.5rem;
}
.header-mark {
    font-size: 0.7rem;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 1.2rem;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
}
.header-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.4rem;
    font-weight: 300;
    color: var(--text);
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 0.8rem;
}
.header-title span { color: var(--accent); }
.header-sub {
    color: var(--muted);
    font-size: 0.88rem;
    font-weight: 300;
    letter-spacing: 0.04em;
    max-width: 480px;
    margin: 0 auto;
    line-height: 1.7;
}

/* ── Textarea ── */
.stTextArea textarea {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
    font-weight: 300 !important;
    line-height: 1.8 !important;
    padding: 1.2rem 1.4rem !important;
    resize: none !important;
    transition: border-color 0.2s ease;
}
.stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: none !important;
}
.stTextArea textarea::placeholder { color: var(--muted) !important; }
.stTextArea label {
    color: var(--muted) !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    font-weight: 500 !important;
}

/* ── Button ── */
.stButton > button {
    background: transparent !important;
    border: 1px solid var(--accent) !important;
    color: var(--accent) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.75rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.25em !important;
    text-transform: uppercase !important;
    padding: 0.85rem 2.8rem !important;
    border-radius: 2px !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    margin-top: 0.5rem;
}
.stButton > button:hover {
    background: var(--accent) !important;
    color: var(--bg) !important;
}

/* ── Result card ── */
.result-card {
    margin-top: 2.5rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    overflow: hidden;
    animation: fadeUp 0.45s ease forwards;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}
.result-band {
    height: 3px;
    width: 100%;
}
.result-body {
    background: var(--surface);
    padding: 2rem 2.2rem;
}
.result-label-row {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 1.4rem;
}
.result-tag {
    font-size: 0.65rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 500;
}
.result-class {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.2rem;
    font-weight: 400;
    letter-spacing: -0.01em;
    line-height: 1;
}
.result-desc {
    color: var(--muted);
    font-size: 0.85rem;
    font-weight: 300;
    line-height: 1.75;
    border-top: 1px solid var(--border);
    padding-top: 1.2rem;
    margin-top: 1.2rem;
}

/* ── Confidence bar ── */
.conf-section { margin-top: 1.6rem; }
.conf-label {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.9rem;
    font-weight: 500;
}
.conf-row {
    display: flex;
    align-items: center;
    gap: 0.9rem;
    margin-bottom: 0.55rem;
}
.conf-name {
    font-size: 0.8rem;
    color: var(--text);
    width: 90px;
    flex-shrink: 0;
    font-weight: 300;
}
.conf-track {
    flex: 1;
    height: 2px;
    background: var(--border);
    border-radius: 99px;
    overflow: hidden;
}
.conf-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s ease;
}
.conf-pct {
    font-size: 0.75rem;
    color: var(--muted);
    width: 38px;
    text-align: right;
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
}

/* ── Disclaimer ── */
.disclaimer {
    margin-top: 3rem;
    padding: 1.2rem 1.6rem;
    border: 1px solid var(--border);
    border-radius: 4px;
    background: var(--surface);
    font-size: 0.78rem;
    color: var(--muted);
    line-height: 1.75;
    font-weight: 300;
    letter-spacing: 0.01em;
}
.disclaimer strong {
    color: var(--accent);
    font-weight: 500;
}

/* ── Footer ── */
.footer {
    text-align: center;
    margin-top: 3.5rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    font-size: 0.72rem;
    color: var(--muted);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 300;
}

/* hide streamlit default padding */
.block-container { padding-top: 0 !important; max-width: 720px !important; }
</style>
""", unsafe_allow_html=True)


# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    encoder = {0: "Depression", 1: "Normal", 2: "Suicidal", 3: "Anxiety", 4: "Stress"}
    return model, encoder

try:
    model, encoder = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    load_error = str(e)

# ── Class config ──────────────────────────────────────────────────────────────
CLASS_CONFIG = {
    "Depression": {
        "color": "#c46e6e",
        "desc": "The analysis indicates markers consistent with depressive patterns — persistent low mood, loss of interest, or feelings of hopelessness. Consider speaking with a mental health professional.",
    },
    "Normal": {
        "color": "#6ea88a",
        "desc": "No significant indicators of mental health distress were detected. The text reflects a generally balanced emotional state.",
    },
    "Suicidal": {
        "color": "#c46e6e",
        "desc": "The analysis detected language associated with suicidal ideation. If you or someone you know is in crisis, please reach out to a mental health professional or crisis line immediately.",
    },
    "Anxiety": {
        "color": "#6e8ec4",
        "desc": "Patterns consistent with anxiety were identified — worry, apprehension, or heightened tension. These feelings are manageable with proper support.",
    },
    "Stress": {
        "color": "#a06ec4",
        "desc": "The text shows indicators of stress — pressure, overwhelm, or difficulty coping. Stress management techniques and professional guidance can help.",
    },
}

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-wrap">
    <div class="header-mark">Mental Health NLP — Analysis Tool</div>
    <div class="header-title">Mind<span>Scan</span></div>
    <div class="header-sub">
        Enter any text to receive an AI-driven analysis of its emotional
        and psychological tone across five clinical categories.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
if not model_loaded:
    st.error(f"Failed to load model: {load_error}")
    st.stop()

text_input = st.text_area(
    "Input Text",
    placeholder="Write or paste any text here — a journal entry, a social media post, or simply how you are feeling today...",
    height=180,
    label_visibility="visible",
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze = st.button("Analyze Text")

# ── Prediction ────────────────────────────────────────────────────────────────
if analyze:
    if not text_input.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        with st.spinner(""):
            try:
                pred = model.predict([text_input])[0]
                label = encoder[int(pred)]
                cfg = CLASS_CONFIG[label]

                color = cfg["color"]

                # Result card
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-band" style="background:{color};"></div>
                    <div class="result-body" style="text-align: center; padding: 2.5rem 1rem;">
                        <span class="result-class" style="color:{color}; font-size: 3rem;">{label}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Prediction error: {e}")

# ── Disclaimer ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="disclaimer">
    <strong>Important Notice</strong> — MindScan is an academic research tool built on machine learning
    and is not a substitute for professional medical advice, diagnosis, or treatment.
    Results should not be used for clinical decision-making. If you are experiencing a mental
    health crisis, please contact a qualified healthcare provider or emergency services.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">MindScan — NLP Mental Health Analysis Tool</div>', unsafe_allow_html=True)
