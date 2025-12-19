import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# --- STYLE & THÈME ---
with st.sidebar:
    st.title("⚙️ SETTINGS")
    dark = st.toggle("🌙 Mode Sombre", value=True)

bg, card, txt, brd, hov = ("#0e1117","#161b22","white","#30363d","#007bff") if dark else ("#f8f9fa","white","black","#eee","red")

st.markdown(f"""<style>
.stApp {{ background-color: {bg}; color: {txt}; }}
.card {{ background:{card}; padding:10px; border-radius:10px; border:1px solid {brd}; text-align:center; height:100px; transition: 0.3s; color: {txt}; display: flex; flex-direction: column; justify-content: center; align-items: center; text-decoration:none!important; }}
.card:hover {{ border-color:{hov}; transform: translateY(-3px); }}
.icon {{ font-size:20px; }}
.title {{ font-size:11px; font-weight:bold; }}
h1, h2, h3, p, span, label, a {{ color: {txt} !important; text-decoration:none!important; }}
</style>""", unsafe_allow_html=True)

# --- SIDEBAR TÂCHES ---
st.sidebar.title("📝 BUREAU")
if 'list' not in st.session_state: st.session_state.list = []
nt = st.sidebar.text_input("Tâche")
if st.sidebar.button("Ajouter") and nt:
    st.session_state.list.append(nt)
    st.rerun()
for i, x in enumerate(st.session_state.list):
    st.sidebar.checkbox(x, key=f"t_{i}")

# --- RECHERCHE ---
st.title("🚀 Sales Cockpit")
c1, c2 = st.columns(2)
with c1:
    g = st.text_input("Google")
    if g: st.write(f"[🔎 Go](https://google.com/search?q={g.replace('
