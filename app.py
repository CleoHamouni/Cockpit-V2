import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# --- STYLE ---
with st.sidebar:
    st.title("SETTINGS")
    dk = st.toggle("Mode Sombre", value=True)

if dk:
    bg, cd, tx, br, hv, sb, bt = "#0e1117", "#161b22", "white", "#30363d", "#007bff", "#161b22", "#0e1117"
else:
    bg, cd, tx, br, hv, sb, bt = "#f8f9fa", "white", "black", "#eee", "red", "#f0f2f6", "white"

st.markdown(f"""<style>
.stApp {{ background-color: {bg}; color: {tx}; }}
[data-testid="stSidebar"] {{ background-color: {sb}; }}
[data-testid="stSidebar"] * {{ color: {tx} !important; }}
.stButton>button {{ background-color: {tx} !important; color: {bt} !important; border: none; font-weight: bold; }}
.card {{ background:{cd}; padding:10px; border-radius:10px; border:1px solid {br}; text-align:center; height:100px; transition: 0.3s; color: {tx}; display: flex; flex-direction: column; justify-content: center; align-items: center; text-decoration:none!important; }}
.card:hover {{ border-color:{hv}; transform: translateY(-3px); }}
.icon {{ font-size:20px; }}
.title {{ font-size:11px; font-weight:bold; }}
h1, h2, h3, p, span, label, a {{ color: {tx} !important; text-decoration:none!important; }}
</style>""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("BUREAU")
if 'L' not in st.session_state: st.session_state['L'] = []
nt = st.sidebar.text_input("Tache")
if st.sidebar.button("Add") and nt:
    st.session_state['L'].append(nt)
