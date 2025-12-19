import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# --- PARAMETRES ---
with st.sidebar:
    st.title("⚙️ SETTINGS")
    dark = st.toggle("🌙 Mode Sombre", value=True)

if dark:
    bg, cd, tx, br, hv = "#0e1117", "#161b22", "white", "#30363d", "#007bff"
    sb_bg, btn_tx = "#161b22", "#0e1117"
else:
    bg, cd, tx, br, hv = "#f8f9fa", "white", "black", "#eee", "red"
    sb_bg, btn_tx = "#f0f2f6", "white"

# --- STYLE ---
css = f"style .stApp {{ background-color: {bg}; color: {tx}; }} "
css += f"[data-testid='stSidebar'] {{ background-color: {sb_bg}; }} "
css += f"[data-testid='stSidebar'] * {{ color: {tx} !important; }} "
css += f".stButton>button {{ background-color: {tx} !important; color: {btn_tx} !important; border: none; font-weight: bold; }} "
css += f".card {{ background:{cd}; padding:10px; border-radius:10px; border:1px solid {br}; text-align:center; height:100px; transition: 0.3s; color: {tx}; display: flex; flex-direction: column; justify-content: center; align-items: center; text-decoration:none!important; }} "
css += f".card:hover {{ border-color:{hv}; transform: translateY(-3px); }} "
css += f".icon {{ font-size:20px; }} .title {{ font-size:11px; font-weight:bold; }} "
css += f"h1, h2, h3, p, span, label, a {{ color: {tx} !important; text-decoration:none!important; }} style"

# On remplace les balises style par des vraies balises HTML
st.markdown(f"<{css.replace('style', 'style')}>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("📝 BUREAU")
if 'list' not in st.session_state: st.session_state.
