from interface.utils import shared_state_counter
import streamlit as st

def render_page2():
    st.title("Ecosystem Overview")
    shared_state_counter()

if __name__ == "__main__":
    render_page1()
#import collections
#from numpy.core.defchararray import lower
#import streamlit as st
#import numpy as np
#import pandas as pd
#from pages import utils
#
#
#
#def app():
#    st.markdown("## Data Upload")
#
#    # Upload the dataset and save as csv
#    st.markdown("### Upload a csv file for analysis.")
#    st.write("\n")
