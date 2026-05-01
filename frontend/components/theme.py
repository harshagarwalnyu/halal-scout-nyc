"""Custom CSS theme for NYC Halal Opportunity Finder."""

import streamlit as st


def inject_custom_theme():
    """Injects production-grade cream/beige editorial theme with green+gold palette."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Lato:ital,wght@0,300;0,400;0,600;0,700;1,400&display=swap');

        /* ── Palette ───────────────────────────────────────────────── */
        :root {
            --primary:      #1a472a;
            --primary-light:#2a6640;
            --accent:       #C9922F;
            --danger:       #c0392b;
            --success:      #2a9d8f;
            --cream:        #F7F3EC;
            --cream-mid:    #EDE8DD;
            --cream-dark:   #E3DDD1;
            --card-bg:      #FFFFFF;
            --text:         #2C2010;
            --text-muted:   #6B5B45;
            --border:       rgba(26, 71, 42, 0.13);
            --border-hover: rgba(201, 146, 47, 0.5);
            --shadow-sm:    0 2px 8px  rgba(44, 32, 16, 0.07);
            --shadow-md:    0 6px 20px rgba(44, 32, 16, 0.10);
            --shadow-hover: 0 10px 28px rgba(44, 32, 16, 0.14);
        }

        /* ── Chrome ────────────────────────────────────────────────── */
        #MainMenu {visibility: hidden;}
        footer     {visibility: hidden;}
        header     {visibility: hidden;}

        /* ── Base ──────────────────────────────────────────────────── */
        .stApp {
            background-color: var(--cream);
            color: var(--text);
            font-family: 'Lato', sans-serif;
        }
        .block-container {
            padding-top: 2rem !important;
            max-width: 1400px;
        }

        /* Typography */
        h1, h2, h3, h4 {
            font-family: 'Playfair Display', Georgia, serif !important;
            color: var(--primary) !important;
            letter-spacing: -0.3px;
        }

        /* Tab panels must match cream bg (not Streamlit default white) */
        [data-baseweb="tab-panel"] {
            background-color: var(--cream) !important;
        }

        /* ── Metric Cards ──────────────────────────────────────────── */
        div[data-testid="stMetric"] {
            background: var(--card-bg);
            border: 1px solid var(--border);
            padding: 1rem 1.2rem;
            border-radius: 12px;
            box-shadow: var(--shadow-sm);
            transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        }
        div[data-testid="stMetric"]:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
            border-color: var(--border-hover);
        }
        div[data-testid="stMetric"] label {
            color: var(--text-muted) !important;
            font-size: 0.78rem !important;
            font-weight: 700 !important;
            text-transform: uppercase;
            letter-spacing: 0.7px;
            font-family: 'Lato', sans-serif !important;
        }
        div[data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: var(--primary) !important;
            font-family: 'Playfair Display', serif !important;
            font-size: 1.35rem !important;
            font-weight: 700;
        }

        /* ── Recommendation Cards ──────────────────────────────────── */
        div[data-testid="stVerticalBlock"] > div[style*="border: 1px solid"] {
            background: var(--card-bg);
            border: 1px solid var(--border) !important;
            border-radius: 16px !important;
            padding: 1.75rem !important;
            margin-bottom: 1.25rem !important;
            box-shadow: var(--shadow-sm);
            transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        div[data-testid="stVerticalBlock"] > div[style*="border: 1px solid"]:hover {
            border-color: var(--border-hover) !important;
            box-shadow: var(--shadow-hover);
            transform: translateY(-3px);
        }

        /* ── Market Badges ─────────────────────────────────────────── */
        .market-badge {
            display: inline-block;
            padding: 0.25rem 0.9rem;
            border-radius: 20px;
            font-size: 0.77rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.7px;
            margin-bottom: 0.5rem;
            font-family: 'Lato', sans-serif;
        }
        .badge-high-opportunity { background:#FDE8E8; color:#c0392b; border:1px solid #e63946; }
        .badge-established-hub  { background:#E3EDF7; color:#2c5f7a; border:1px solid #457b9d; }
        .badge-growing-market   { background:#E8F5E9; color:#1e7a6e; border:1px solid #2a9d8f; }
        .badge-low-demand       { background:#F5F0E8; color:#5C5246; border:1px solid #B0A898; }

        /* ── Sidebar ───────────────────────────────────────────────── */
        section[data-testid="stSidebar"] {
            background-color: var(--cream-mid);
            border-right: 1px solid var(--border);
        }
        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] .stSlider label {
            color: var(--primary) !important;
            font-weight: 700 !important;
            font-size: 0.80rem !important;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }

        /* ── Progress Bars ─────────────────────────────────────────── */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, var(--primary), var(--accent)) !important;
            border-radius: 4px;
        }

        /* ── Tabs ──────────────────────────────────────────────────── */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.25rem;
            background-color: transparent;
            border-bottom: 2px solid var(--border);
            padding-bottom: 0;
        }
        .stTabs [data-baseweb="tab"] {
            height: 48px;
            background-color: transparent;
            border-radius: 8px 8px 0 0;
            padding: 10px 22px;
            color: var(--text-muted);
            font-family: 'Lato', sans-serif;
            font-weight: 600;
            font-size: 0.88rem;
            letter-spacing: 0.3px;
            transition: color 0.2s ease, background-color 0.2s ease;
            border-bottom: 3px solid transparent;
        }
        .stTabs [data-baseweb="tab"]:hover {
            color: var(--primary);
            background-color: rgba(26, 71, 42, 0.04);
        }
        .stTabs [aria-selected="true"] {
            background-color: rgba(26, 71, 42, 0.05);
            border-bottom: 3px solid var(--primary) !important;
            color: var(--primary) !important;
            font-weight: 700;
        }

        /* ── Buttons ───────────────────────────────────────────────── */
        .stButton > button {
            border-radius: 8px;
            border: 1.5px solid var(--primary);
            background-color: transparent;
            color: var(--primary);
            font-family: 'Lato', sans-serif;
            font-weight: 700;
            font-size: 0.84rem;
            letter-spacing: 0.5px;
            transition: all 0.2s ease;
            padding: 0.5rem 1.25rem;
        }
        .stButton > button:hover {
            background-color: var(--primary);
            color: var(--cream);
            box-shadow: var(--shadow-sm);
        }
        .stButton > button:active {
            transform: scale(0.98);
        }

        /* ── Expanders ─────────────────────────────────────────────── */
        .stExpander {
            border: 1px solid var(--border) !important;
            border-radius: 10px !important;
            background: var(--card-bg) !important;
            margin-bottom: 0.5rem;
        }
        details summary {
            font-family: 'Lato', sans-serif;
            font-weight: 700;
            color: var(--text);
            font-size: 0.9rem;
        }

        /* ── Alert boxes ───────────────────────────────────────────── */
        div[data-testid="stInfo"] {
            background-color: rgba(26, 71, 42, 0.06);
            border-left: 3px solid var(--primary);
            border-radius: 6px;
            color: var(--text);
        }
        div[data-testid="stWarning"] {
            background-color: rgba(201, 146, 47, 0.09);
            border-left: 3px solid var(--accent);
            border-radius: 6px;
        }
        div[data-testid="stSuccess"] {
            background-color: rgba(42, 157, 143, 0.09);
            border-left: 3px solid var(--success);
            border-radius: 6px;
        }

        /* ── Divider ───────────────────────────────────────────────── */
        hr {
            border-color: var(--border) !important;
            opacity: 1;
        }

        /* ── Caption / small text ──────────────────────────────────── */
        .stCaption, small, [data-testid="stCaptionContainer"] {
            color: var(--text-muted) !important;
            font-family: 'Lato', sans-serif;
            font-size: 0.82rem !important;
        }

        /* ── DataFrames ────────────────────────────────────────────── */
        [data-testid="stDataFrame"] {
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid var(--border);
        }

        /* ── Download button ───────────────────────────────────────── */
        .stDownloadButton > button {
            border-radius: 8px;
            background-color: var(--primary);
            color: var(--cream);
            font-family: 'Lato', sans-serif;
            font-weight: 700;
            font-size: 0.84rem;
            border: none;
            transition: all 0.2s ease;
        }
        .stDownloadButton > button:hover {
            background-color: var(--primary-light);
            box-shadow: var(--shadow-md);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
