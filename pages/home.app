import collections
from numpy.core.defchararray import lower
import streamlit as st
import numpy as np
import pandas as pd
from pages import utils



def app():
    st.markdown("## Data Upload")

    # Upload the dataset and save as csv
    st.markdown("### Upload a csv file for analysis.") 
    st.write("\n")
