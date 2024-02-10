import streamlit as st
import os
import time
import base64
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    initial_sidebar_state ="collapsed",
    page_title="Visualization"
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
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    if st.button("Home"):
        switch_page("Home")
with col4:
    if st.button("Search"):
        switch_page("Search")
with col5:
    if st.button("Visualization"):
        switch_page("Visualization")
@st.cache_data
def get_img_as_base64(file):
    with open(file,"rb") as f:
        data=f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("nav_bar.jpg")

def header(txt):
    st.markdown(f'<p style="background-color:rgba(0,0,0,0);color:#ffffff;font-size:36px;border-radius:2%;">{txt}</p>', unsafe_allow_html=True)
@st.cache_resource
def page_style():
    header("Main Page")
    header("Content")
    html_code = f"""
    <style>
    div[data-testid="stButton"] button{{
    background-color: rgba(0,0,0,0);
    color: #ffffff;
    border: none;
    position: fixed;
    top: 25px;
    transform: translateX(+120%);
    cursor: pointer;
    transition: color 0.3s ease;
    }}
    div[data-testid="stButton"] button:hover{{
    color: #bfbfbf;
    }}
    div[data-testid="stButton"] button:active{{
    background-color: rgba(0,0,0,0);
    color: #cccccc;
    }}
    div[data-testid="stSidebarNav"] li div a {{
            margin-left: 1rem;
            padding: 1rem;
            width: 300px;
            border-radius: 0.5rem;
    }}
    div[data-testid="stSidebarNav"] li div::focus-visible {{
            background-color: rgba(151, 166, 195, 0.15);
        }}
    [data-testid="stAppViewContainer"] {{
    background-image: url("https://www.kai-stiepel.com/wp-content/uploads/2016/11/mediterrane_kueche-1400x925.jpg");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    }}
    [data-testid="stSidebarContent"] {{
    background-image: url("data:image/png;base64,{img}");
    background-size: center;
    }}
    div[data-testid="stSidebarNav"] li div a span {{
    color: #ffffff
    }}
    div[data-testid="stSidebarNav"] li div a[href="http://localhost:8502/"]::before {{
        content: url('https://img.icons8.com/ffffff/ios/25/home--v1.png'); 
        margin-right: 5px;
        color: white;
        
    }}
    div[data-testid="stSidebarNav"] li div a[href="http://localhost:8502/Visualization"]::before {{
        content: url('https://img.icons8.com/ffffff/external-flaticons-lineal-flat-icons/25/external-dashboard-computer-programming-flaticons-lineal-flat-icons.png'); 
        margin-right: 5px;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0)
    }}

    [data-testid="stToolbar]{{
    right: 2rem;
    }}
    </style>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    #html_file = open("transparent_nav.html")
    #html(html_file.read(), height=100%, width=100%)

    with st.container():
        header("Header 1")
        html='''
    <p style="color:white">Lorem ipsum <em>dolor</em> sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    '''
    st.markdown(html, unsafe_allow_html=True)
    with st.container():
        header("Header 2")
        html='''
    <p style="color:white">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    '''
    st.markdown(html, unsafe_allow_html=True)
    with st.container():
        header("Header 3")
        html='''
    <p style="color:white">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    '''
    st.markdown(html, unsafe_allow_html=True)
    with st.container():
        header("Header 4")
        html='''
    <p style="color:white">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    '''
    st.markdown(html, unsafe_allow_html=True)


    #with st.sidebar:
        #selected = option_menu(
            #menu_title = None,
            #options = ["Search","Visualization","Reference"],
            #icons = ["search","clipboard-data","bookmarks"],
            #orientation = "horizontal"

    #)
page_style()
