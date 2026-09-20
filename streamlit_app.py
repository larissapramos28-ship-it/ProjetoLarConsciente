import streamlit as st
import streamlit.components.v1 as components

SITE_URL = "https://projeto-lar-consciente.laryssaramos2807.chatgpt.site"
admin_mode = st.query_params.get("painel") == "administrativo"

st.set_page_config(
    page_title="Painel Administrativo" if admin_mode else "Projeto Lar Consciente",
    page_icon="🔐" if admin_mode else "🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .stAppHeader, [data-testid="stSidebarCollapsedControl"], footer { display: none; }
      .block-container { max-width: 100%; padding: 0; }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

page_url = f"{SITE_URL}/login.html?versao=6" if admin_mode else f"{SITE_URL}/?versao=6"

components.iframe(
    page_url,
    height=1200,
    scrolling=True,
)
