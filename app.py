import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_folium import folium_static
import folium
from pyairtable import Table
import geopandas as gpd
from PIL import Image
import requests

import streamlit as st
from interface.home import render_page1
from interface.ecosystem import render_page2
from interface.sector import render_page3

if 'count' not in st.session_state:
    st.session_state.count = 0

def render():
    pages = {
        "Page 1": render_page1,
        "Page 2": render_page2,
        "Page 3": render_page3
    }

    st.sidebar.title("Streamlit Multi-page App")
    selected_page = st.sidebar.radio("Select a page", options=list(pages.keys()))

    pages[selected_page]()


if __name__ == "__main__":
    render()


#from multipage import MultiPage
#from pages import home, ecosystem, sector
#
##https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/
##https://docs.streamlit.io/library/advanced-features/configuration
##https://miro.com/app/board/uXjVOQGY1Do=/
#
#
## Create an instance of the app
#app = MultiPage()
#
## Title of the main page
#st.title("NYC Tech Ecosystem")
#
## Add all your applications (pages) here
#app.add_page("Home", home.app)
#app.add_page("Ecosystem Overview", ecosystem.app)
#app.add_page("Sector Profile", sector.app)
#
## The main app
#app.run()


