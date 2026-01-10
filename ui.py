import streamlit as st

def apply_custom_ui():
    MAIN_BG = "#7aa1ee"  # Netflix Dark Theme
    SIDEBAR_BG = "#02309b" # Deep Blue Sidebar

    st.markdown(f"""
    <style>
    /* Main Background */
    html, body, [data-testid="stApp"] {{ 
        background-color: {MAIN_BG}; 
        color: white;
    }}
    
    /* Sidebar Background */
    section[data-testid="stSidebar"] {{ 
        background-color: {SIDEBAR_BG} !important; 
    }}

    /* Sidebar Text & Label Visibility */
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: white !important;
    }}

    /* Remove Metric Boxes (Transparent Look) */
    div[data-testid="metric-container"] {{
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}
    [data-testid="stMetricValue"] {{ color: #E50914 !important; font-size: 32px !important; }}
    [data-testid="stMetricLabel"] {{ color: #ffffff !important; }}

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {{ gap: 24px; }}
    .stTabs [data-baseweb="tab"] {{ height: 50px; font-weight: bold; color: white; }}
    .stTabs [aria-selected="true"] {{ color: #E50914 !important; border-bottom-color: #E50914 !important; }}

    header[data-testid="stHeader"] {{ visibility: hidden; }}
    </style>
    """, unsafe_allow_html=True)