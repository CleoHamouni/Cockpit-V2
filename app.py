import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Sales Cockpit Hub", page_icon="💼", layout="wide")

# --- GESTION DU THÈME ---
with st.sidebar:
    st.title("👨‍✈️ Configuration")
    dark_mode = st.toggle("🌙 Mode Sombre", value=False)

# Définition des couleurs selon le mode
if dark_mode:
    bg_color = "#121212"      # Noir profond
    card_bg = "#1E1E1E"       # Gris foncé
    text_color = "#FFFFFF"    # Blanc
    border_color = "#333333"  # Gris léger
    sub_text = "#AAAAAA"      # Gris clair pour les descriptions
else:
    bg_color = "#F0F2F6"      # Gris clair
    card_bg = "#FFFFFF"       # Blanc
    text_color = "#000000"    # Noir
    border_color = "#EEEEEE"  # Gris très clair
    sub_text = "#666666"      # Gris moyen

# --- INJECTION DU CSS DYNAMIQUE ---
st.markdown(f"""
    <style>
    /* Fond de l'application */
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    
    /* Style des cartes */
    .card {{
        padding: 25px;
        border-radius: 15px;
        background-color: {card_bg};
        border: 1px solid {border_color};
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }}
    .card:hover {{
        transform: translateY(-5px);
        border-color: #007bff;
    }}
    .card h3 {{
        color: {text_color} !important;
        margin-bottom: 10px;
    }}
    .card p {{
        color: {sub_text};
    }}
    
    /* Boutons */
    .stButton>button {{
        width: 100%;
        border-radius: 10px;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }}
    
    /* Titres Streamlit */
    h1, h2, h3, p {{
        color: {text_color} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE (NAVIGATION) ---
with st.sidebar:
    st.subheader("🛠 Mes Outils")
    
    # BOUTON VERS TA NOUVELLE APPLI CV
    st.link_button("🎯 Ouvrir l'Analyseur de CV", "https://cv-optimizer-pro-idiwl9xcvopi6orfgqyhjp.streamlit.app/")
    
    st.divider()
    st.caption(f"Sales Cockpit v2.1 | Mode: {'Sombre' if dark_mode else 'Clair'}")

# --- CONTENU PRINCIPAL ---
st.title("💼 Sales Cockpit : Tableau de Bord")
st.write("Bienvenue dans votre centre de pilotage intelligent.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""<div class="card">
        <h3>📈 Performance</h3>
        <p>Suivez vos KPIs de vente en temps réel et analysez votre croissance.</p>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""<div class="card">
        <h3>🤝 CRM Quick Access</h3>
        <p>Retrouvez vos derniers échanges clients et relances prioritaires.</p>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""<div class="card">
        <h3>📄 Staffing IA</h3>
        <p>Utilisez l'intelligence artificielle pour matcher vos candidats et vos offres.</p>
    </div>""", unsafe_allow_html=True)
    st.link_button("Lancer l'Analyseur CV", "https://cv-optimizer-pro-idiwl9xcvopi6orfgqyhjp.streamlit.app/")

st.divider()

# Section Rappels
st.subheader("📅 Rappels du jour")
c_col1, c_col2 = st.columns(2)
with c_col1:
    st.checkbox("Relancer le client de l'annonce CV")
    st.checkbox("Vérifier les nouveaux crédits OpenAI")
with c_col2:
    st.checkbox("Préparer la réunion commerciale")
    st.checkbox("Mettre à jour le CRM")
