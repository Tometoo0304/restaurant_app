import streamlit as st
import os
import time
import base64
from streamlit.components.v1 import html, iframe
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu

st.set_page_config(
    initial_sidebar_state ="collapsed",
    page_title="user guide"
)
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

#html_file = open("nyc_restaurant_map.html")
import requests
from bs4 import BeautifulSoup

iframe("./html/nyc_restaurant_map.html", height=1000, width=1000)
