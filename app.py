import json
import os
import streamlit as st

# Configurazione della pagina ottimizzata per mobile
st.set_page_config(
    page_title="Statbot Leagues Hub", page_icon="🏆", layout="centered"
)

# CSS personalizzato per compattare gli elementi su mobile
st.markdown("""
    <style>
        .server-card {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px;
            border: 1px solid rgba(250, 250, 250, 0.2);
            border-radius: 8px;
            margin-bottom: 10px;
            background-color: rgba(255, 255, 255, 0.03);
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏆 Statbot - Hub")
st.write("Seleziona una lega:")
st.divider()

def carica_configurazione():
    try:
        with open("server_links.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

data = carica_configurazione()

if data:
    for server_id, info in data.items():
        channel_name = info.get("channel_name", f"Server {server_id}")
        logo_filename = info.get("logo_filename", "logo.png")
        url_risultati = info.get("url_risultati", "#")
        
        logo_path = os.path.join("static", logo_filename)
        if not os.path.exists(logo_path):
            logo_path = "static/logo.png"

        # Layout a riga compatta per mobile: [Icona] [Nome] [Bottone]
        cols = st.columns([1.2, 3.5, 2.5])
        
        with cols[0]:
            st.image(logo_path, width=45)
            
        with cols[1]:
            st.markdown(f"**{channel_name}**")
            
        with cols[2]:
            st.link_button("🚀 Apri", url_risultati, width='stretch')
            
        st.divider()
else:
    st.error("⚠️ File `server_links.json` non trovato.")