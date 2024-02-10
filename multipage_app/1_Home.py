import streamlit as st
import os
import time
import base64
from streamlit.components.v1 import html, iframe
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu

st.set_page_config(
    initial_sidebar_state ="collapsed",
    page_title="Hello"
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
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col3:
    if st.button("Home"):
        switch_page("Home")
with col4:
    if st.button("Search"):
        switch_page("Search")
with col5:
    if st.button("Visualization"):
        switch_page("Visualization")
with col6:
    if st.button("Experiment"):
        switch_page("Experiment")

#st.page_link("https://www.google.com/", label="Home")
#st.page_link("pages/2_Visualization.py", label="Visualization")
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
    header("Homer")
    header("content")
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
#html_file = open("transparent_nav.html")
#html(html_file.read(), height=1000, width=1000, scrolling=True)
#iframe("http://www.bing.com", height= 500, width=1000)
import xyzservices.providers as xyz

from bokeh.plotting import figure, show
import pygsheets
import numpy as np
# range bounds supplied in web mercator coordinates
import folium
from folium.plugins import FastMarkerCluster, MarkerCluster
from streamlit_folium import st_folium
#map = folium.Map(location=[40.7128, -74.0060], zoom_start=5)
#marker_cluster = FastMarkerCluster(data=list(zip(df['latitude'], df['longitude'])), popup=list(df['popup']))
@st.cache_data
def read_data():
    gs = pygsheets.authorize(service_file="C:/Users/wangj/Desktop/data/banded-oven-412622-bcdb12f463f1.json")
    workbook = gs.open('nyc_restaurant_inspections') 
    restaurant = workbook[0].get_as_df(numerize=False)
    restaurant = restaurant.replace("", np.nan)
    restaurant[["latitude","longitude"]] = restaurant[["latitude","longitude"]].astype(float)
    return restaurant
restaurant = read_data()
map = folium.Map(location=[40.7128, -74.0060], zoom_start=5)
locations = list(zip(restaurant['latitude'], restaurant['longitude']))
popups = ['Latitude:{}<br>Longitude:{}'.format(lat, lon) for (lat, lon) in locations]
#marker_cluster = MarkerCluster(locations=locations,popups=popups)
marker_cluster = FastMarkerCluster(data=[])
#marker_cluster = FastMarkerCluster(data=locations).add_to(map)
for coordinate in locations:
    folium.Marker(location=[coordinate[0],coordinate[1]],popup=f'Latitude:{coordinate[0]}<br>Longitude:{coordinate[1]}').add_to(marker_cluster)

marker_cluster.add_to(map)
folium.LayerControl().add_to(map)
st_data = st_folium(map, width=800)