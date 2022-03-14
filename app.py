import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_folium import folium_static
import folium
from pyairtable import Table
import geopandas as gpd
from PIL import Image
import requests

from multipage import MultiPage
from pages import home, ecosystem, sector

#https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/
#https://docs.streamlit.io/library/advanced-features/configuration
#https://miro.com/app/board/uXjVOQGY1Do=/


# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("NYC Tech Ecosystem")

# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Ecosystem Overview", ecosystem.app)
app.add_page("Sector Profile", sector.app)

# The main app
app.run()


