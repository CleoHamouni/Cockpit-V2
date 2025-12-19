import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# --- SETTINGS ---
with st.sidebar:
    st.title("SETTINGS")
    dk = st.toggle("Mode Sombre", value=True)

# Couleurs
if dk:
    bg, cd, tx, br, sb = "#0e1117", "#ffffff", "#000000", "#30363d", "#161b22"
else:
    bg, cd, tx, br, sb = "#f8f9fa", "#ffffff", "#000000", "#eee", "#f0f2f6"

# --- STYLE CSS ---
st.markdown(f"""
<style>
.stApp {{ background-color: {bg}; }}
[data-testid="stSidebar"] {{ background-color: {sb}; }}
.card {{
    background-color: white !important;
    padding: 15px;
    border-radius: 10px;
    border: 2px solid {br};
    text-align: center;
    height: 110px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}}
.card:hover {{ border-color: #007bff; transform: scale(1.02); }}
.icon {{ font-size: 30px; margin-bottom: 5px; }}
.title {{ font-size: 13px; font-weight: bold; color: black !important; }}
a {{ text-decoration: none !important; }}
/* Force le texte de la recherche en blanc si mode sombre */
label, p {{ color: {"white" if dk else "black"} !important; }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("BUREAU")
