import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Projeto Lar Consciente",
    page_icon="🏠",
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

components.iframe(
    "https://projeto-lar-consciente.laryssaramos2807.chatgpt.site/?versao=3",
    height=1200,
    scrolling=True,
)
