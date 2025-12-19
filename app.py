import streamlit as st

st.set_page_config(page_title="IA Cockpit", layout="wide")

# --- INTERRUPTEUR DE THÈME ---
with st.sidebar:
    st.title("⚙️ SETTINGS")
    dark_mode = st.toggle("🌙 Mode Sombre", value=True)

# Définition des couleurs dynamiques
if dark_mode:
    bg_color = "#0e1117"
    card_bg = "#161b22"
    text_color = "white"
    border_color = "#30363d"
    hover_color = "#007bff" # Bleu néon au survol
else:
    bg_color = "#f8f9fa"
    card_bg = "white"
    text_color = "black"
    border_color = "#eee"
    hover_color = "red" # Ton rouge d'origine

# CSS DYNAMIQUE
st.markdown(f"""
<style>
.stApp {{ background-color: {bg_color}; }}
.card {{
    background:{card_bg}; 
    padding:10px; 
    border-radius:10px;
    border:1px solid {border_color};
    text-align:center; 
    height:120px; 
    transition: 0.3s;
    color: {text_color};
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}}
.card:hover {{
    border-color:{hover_color}; 
    transform: translateY(-5px); 
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}}
.icon {{ font-size:25px; margin-bottom: 5px; }}
.title {{ font-size:12px; font-weight:bold; color: {text_color}; }}
a {{ text-decoration:none!important; }}
h1, h2, h3, p, span, label {{ color: {text_color} !important; }}
</style>
""", unsafe_allow_html=True)

# SIDEBAR BUREAU
st.sidebar.title("📝 BUREAU")
if 'list' not in st.session_state: st.session_state.list = []
new_t = st.sidebar.text_input("Nouvelle tâche")
if st.sidebar.button("Ajouter"):
    if new_t:
        st.session_state.list.append(new_t)
        st.rerun()

for i, x in enumerate(st.session_state.list):
    st.sidebar.checkbox(x, key=f"t_{i}")

# RECHERCHE
st.title("🚀 Sales Cockpit")
c1, c2 = st.columns(2)
with c1:
    g = st.text_input("Google Search")
    if g:
        u_g = "https://www.google.com/search?q=" + g.replace(' ', '+')
        st.markdown(f"[🔎 Lancer la recherche]({u_g})")
with c2:
    l = st.text_input("LinkedIn Search")
    if l:
        u_l = "https://www.linkedin.com/search/results/all/?keywords=" + l.replace(' ', '%20')
        st.markdown(f"[👤 Trouver le profil]({u_l})")

st.divider()

# APPLIS
b = "https://"
s = ".streamlit.app/"

u1 = b + "cv-optimizer-pro-idiwl9xcvopi6orfgqyhjp" + s
u2 = b + "freelancevscollab-" + "tcjdkokhjktthqet9emwd2" + s
u3 = b + "go-nogo-ao-" + "guljf7vfdgd8gwbwk2czss" + s
u4 = b + "ia-discovery-tool-" + "exipby6qyeqodoryc8p7kj" + s
u5 = b + "objection-crusher-" + "eickr9egabodnbspah7zgh" + s
u6 = b + "sales-kpi-tracker-" + "gemm7zlpac7rv5hdkfyesy" + s
u7 = b + "simulateuria-" + "4geraztakpppefxpsvfp5z" + s
u8 = b + "account-manager-ia-" + "hwtkfcycxcxcgqtxrhyrez" + s

tools = [
    ("CV Optimizer", "🎯", u1), ("Marge/Rentab", "⚖️", u2),
    ("Go/No-Go AO", "🚦", u3), ("IA Discovery", "🔍", u4),
    ("Objection", "
