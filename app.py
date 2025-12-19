import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# --- THÈME ---
with st.sidebar:
    st.title("⚙️ SETTINGS")
    dark_mode = st.toggle("🌙 Mode Sombre", value=True)

if dark_mode:
    bg, card, txt, border, hover = "#0e1117", "#161b22", "white", "#30363d", "#007bff"
else:
    bg, card, txt, border, hover = "#f8f9fa", "white", "black", "#eee", "red"

st.markdown(f"""
<style>
.stApp {{ background-color: {bg}; }}
.card {{
    background:{card}; padding:10px; border-radius:10px; border:1px solid {border};
    text-align:center; height:120px; transition: 0.3s; color: {txt};
    display: flex; flex-direction: column; justify-content: center; align-items: center;
}}
.card:hover {{ border-color:{hover}; transform: translateY(-5px); box-shadow: 0px 4px 15px rgba(0,0,0,0.3); }}
.icon {{ font-size:25px; }}
.title {{ font-size:12px; font-weight:bold; color: {txt}; }}
a {{ text-decoration:none!important; }}
h1, h2, h3, p, span, label {{ color: {txt} !important; }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("📝 BUREAU")
if 'list' not in st.session_state: st.session_state.list = []
new_t = st.sidebar.text_input("Tâche")
if st.sidebar.button("Ajouter"):
    if new_t:
        st.session_state.list.append(new_t)
        st.rerun()
for i, x in enumerate(st.session_state.list):
    st.sidebar.checkbox(x, key=f"t_{i}")

# --- CONTENU ---
st.title("🚀 Sales Cockpit")
c1, c2 = st.columns(2)
with c1:
    g = st.text_input("Google Search")
    if g: st.markdown(f"[🔎 Go](https://www.google.com/search?q={g.replace(' ', '+')})")
with c2:
    l = st.text_input("LinkedIn Search")
    if l: st.markdown(
