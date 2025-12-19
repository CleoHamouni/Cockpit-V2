import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# --- SETTINGS ---
with st.sidebar:
    st.title("⚙️ SETTINGS")
    dark = st.toggle("🌙 Mode Sombre", value=True)

if dark:
    bg, cd, tx, br, hv = "#0e1117", "#161b22", "white", "#30363d", "#007bff"
else:
    bg, cd, tx, br, hv = "#f8f9fa", "white", "black", "#eee", "red"

st.markdown(f"""<style>
.stApp {{ background-color: {bg}; color: {tx}; }}
.card {{ background:{cd}; padding:10px; border-radius:10px; 
border:1px solid {br}; text-align:center; height:100px; 
transition: 0.3s; color: {tx}; display: flex; 
flex-direction: column; justify-content: center; 
align-items: center; text-decoration:none!important; }}
.card:hover {{ border-color:{hv}; transform: translateY(-3px); }}
.icon {{ font-size:20px; }}
.title {{ font-size:11px; font-weight:bold; }}
h1, h2, h3, p, span, label, a {{ color: {tx} !important; 
text-decoration:none!important; }}
</style>""", unsafe_allow_html=True)

# --- SIDEBAR ---
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
    if g:
        q_g = g.replace(' ','+')
        st.write(f"[🔎 Go](https://google.com/search?q={q_g})")
with c2:
    l = st.text_input("LinkedIn")
    if l:
        q_l = l.replace(' ','%20')
        st.write(f"[👤 Go](https://linkedin.com/search/results/all/?keywords={q_l})")

st.divider()

# --- APPLIS ---
s = ".streamlit.app/"
apps = [
    ("CV Optimizer", "🎯", "cv-optimizer-pro-idiwl9xcvopi6orfgqyhjp"),
    ("Marge/Rentab", "⚖️", "freelancevscollab-tcjdkokhjktthqet9emwd2"),
    ("Go/No-Go AO", "🚦", "go-nogo-ao-guljf7vfdgd8gwbwk2czss"),
    ("IA Discovery", "🔍", "ia-discovery-tool-exipby6qyeqodoryc8p7kj"),
    ("Objection", "🛡️", "objection-crusher-eickr9egabodnbspah7zgh"),
    ("KPI Tracker", "📈", "sales-kpi-tracker-gemm7zlpac7rv5hdkfyesy"),
    ("Simu Salaire", "🤖", "simulateuria-4geraztakpppefxpsvfp5z"),
    ("Account Mgr", "🤝", "account-manager-ia-hwtkfcycxcxcgqtxrhyrez")
]

cols = st.columns(4)
for i, (name, icon, url) in enumerate(apps):
    with cols[i % 4]:
        link = f"https://{url}{s}"
        html = f"""<a href="{link}" target="_blank">
        <div class="card">
        <div class="icon">{icon}</div>
        <div class="title">{name}</div>
        </div></a>"""
        st.markdown(html, unsafe_allow_html=True)
        st.write("")
