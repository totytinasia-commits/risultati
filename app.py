import json
import os
import streamlit as st

# Configurazione della pagina ottimizzata per mobile
st.set_page_config(
    page_title="Statbot Leagues Scrims Result", page_icon="🏆", layout="centered"
)

st.title("🏆 Statbot - Scrims Result")
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
        
        # Eventuale secondo link opzionale (es. per Clans League)
        url_secondario = info.get("url_secondario", None)
        testo_secondario = info.get("testo_secondario", "Extra")
        
        logo_path = os.path.join("static", logo_filename)
        if not os.path.exists(logo_path):
            logo_path = "static/logo.png"

        # Se ci sono 2 pulsanti, ridistribuiamo le colonne in modo ottimale per mobile
        if url_secondario:
            cols = st.columns([1.0, 2.5, 1.8, 1.8])
            with cols[0]:
                st.image(logo_path, width=40)
            with cols[1]:
                st.markdown(f"**{channel_name}**")
            with cols[2]:
                st.link_button("🚀 Apri", url_risultati, width='stretch')
            with cols[3]:
                st.link_button(f"📊 {testo_secondario}", url_secondario, width='stretch')
        else:
            # Layout standard a 1 pulsante
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
