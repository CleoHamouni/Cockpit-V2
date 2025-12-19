import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# --- THÈME ---
with st.sidebar:
    st.title("⚙️ SETTINGS")
    dark = st.toggle("🌙 Mode Sombre", value=True)

if dark:
    bg, card, txt, brd, hov = "#0e1117", "#161b22", "white", "#30363d", "#007bff"
else:
    bg, card, txt, brd, hov = "#f8f9fa", "white", "black", "#eee", "red"

st.markdown(f"""
<style>
.stApp {{ background-color: {bg}; }}
.card {{
    background:{card}; padding:10px; border-radius:10px; border:1px solid {brd};
    text-align:center; height:110px; transition: 0.3s; color: {txt};
    display: flex; flex-direction: column; justify-content: center; align-items: center;
}}
.card:hover {{ border-color:{hov}; transform: translateY(-5px); }}
.icon {{ font-size:22px; }}
.title {{ font-size:11px; font-weight:bold; color: {txt}; }}
a {{ text-decoration:none!important; }}
h1, h2, h3, p, span, label {{ color: {txt} !important; }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("📝 BUREAU")
if 'list' not in st.session_state: st.session_state.list = []
nt = st.sidebar.text_input("Tâche")
if st.sidebar.button("Ajouter") and nt:
    st.session_state.list.append(nt)
    st.rerun()
for i, x in enumerate(st.session_state.list):
    st.sidebar.checkbox(x, key=f"t_{i}")

# ---
