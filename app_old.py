import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_folium import folium_static
import folium
from pyairtable import Table
import geopandas as gpd
from PIL import Image
import requests

#https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/
#https://docs.streamlit.io/library/advanced-features/configuration
#https://miro.com/app/board/uXjVOQGY1Do=/

#import airtable
api_key = 'keyfr6BmiKOdAURea' ## prekshA's api key
base_id = "apptUkOtU3W8HxbQQ"
table_name = "Organization List"
table = Table(api_key, base_id, table_name)
all_data = table.all()
df_tech = pd.json_normalize(all_data, sep='_')

#parse airtable
def parse_cat(x):
    if type(x) is not list:
        return ''
    st = ''.join(str(e) for e in x)
    return st

#filter data
df_passed = df_tech[df_tech['fields_Urban Tech Screening'] == 'Passed']
df_passed['fields_Category'] = df_passed['fields_Category'].apply(lambda x: parse_cat(x))
df_passed['fields_Sub-category'] = df_passed['fields_Sub-category'].apply(lambda x: parse_cat(x))

# make df
datasource_url="https://www.fhwa.dot.gov/bridge/nbi/2021/delimited/NJ21.txt"
#datasource_url="https://docs.google.com/spreadsheets/d/e/2PACX-1vS-sKp0sa-WwtAzw4-2ioiD5-Mtb0BLL1Ju2ZMNfkib5kLQ8blYzQ6YmikyrBtNKA/pub?output=csv"
df = pd.read_csv(datasource_url)

# Read in NYC shapefile and check shape
#nyc = gpd.read_file('modzcta_shp/geo_export_682e39f4-a884-431b-91b2-5927fe09ccd4.shp')

#geometry = [Point(xy) for xy in zip(df_passed['fields_Longitude'], df_passed['fields_Latitude'])]
#geo_df_passed = gpd.GeoDataFrame(df_passed, crs=nyc.crs, geometry=geometry)


# filter by county
df = df.loc[df['COUNTY_CODE_003'] == 17]

# convert degrees,minutes, seconds to decimal degrees
df['lat_deg'] = df['LAT_016'].apply(lambda x: str(x)[0:2])
df['lat_min'] = df['LAT_016'].apply(lambda x: str(x)[2:4])
df['lat_sec'] = df['LAT_016'].apply(lambda x: str(x)[4:6])
df['lat_hem'] = df['LAT_016'].apply(lambda x: str(x)[6:8])
df['lon_deg'] = df['LONG_017'].apply(lambda x: str(x)[0:2])
df['lon_min'] = df['LONG_017'].apply(lambda x: str(x)[2:4])
df['lon_sec'] = df['LONG_017'].apply(lambda x: str(x)[4:6])
df['lon_hem'] = df['LONG_017'].apply(lambda x: str(x)[6:8])
def lat_dms2dd(row):
    dd = float(row.lat_deg) + float(row.lat_min)/60 + float(row.lat_sec)/(60*60)
    return dd
def lon_dms2dd(row):
    dd = float(row.lon_deg) + float(row.lon_min)/60 + float(row.lon_sec)/(60*60)
    dd *= -1
    return dd
df['lat'] = df.apply(lambda x: lat_dms2dd(x), axis=1)
df['lon'] = df.apply(lambda x: lon_dms2dd(x), axis=1)

# drop weird outliers
indexNames = df[ (df.lon > -70) ].index
df.drop(indexNames , inplace=True)
indexNames = df[ (df.lon < -80) ].index
df.drop(indexNames , inplace=True)

# # create map
# map = folium.Map(location=[40.7178, -74.10], zoom_start=12, tiles ='Stamen Toner')
map = folium.Map(location=[40.7168, -73.9910], zoom_start=12)

# populate popups
def render_popup(row):
    #FIXME: the weird line at the top
    html_data = [f"<tr><td>{label}</td><td>{value}</td></tr>" for (label, value) in row.items()]
    html=f"""
    <h3> {row.FEATURES_DESC_006A.strip("'")} ({row.STRUCTURE_NUMBER_008})</h3>
    <h4> Structural evaluation rating {row.STRUCTURAL_EVAL_067} out of 9</h4>
    <table>
    {''.join([str(x) for x in html_data])}
    </table>
    """
    iframe = folium.IFrame(html=html, width=500, height=300)
    return folium.Popup(iframe, max_width=500)

# # create markers
# for index, row in df.iterrows():
#     tooltip = f"Structure No.{row.STRUCTURE_NUMBER_008} built in {row.YEAR_BUILT_027}. Structural rating {row.STRUCTURAL_EVAL_067} out of 9."
#     structural_rating = int(row.STRUCTURAL_EVAL_067)
#     if structural_rating <= 3:
#         folium.CircleMarker([row["lat"],row["lon"]],
#                     color='red',
#                     radius=3,
#                     popup=render_popup(row),
#                     tooltip=tooltip
#                     ).add_to(map)
#     elif structural_rating in range(4,5):
#         folium.CircleMarker([row["lat"],row["lon"]],
#                     color='yellow',
#                     radius=3,
#                     popup=render_popup(row),
#                     tooltip=tooltip
#                     ).add_to(map)
#     else:
#         folium.CircleMarker([row["lat"],row["lon"]],
#                     color='gray',
#                     radius=3,
#                     popup=render_popup(row),
#                     tooltip=tooltip
#                     ).add_to(map)

## navigating between pages using streamlit radio
my_page = st.sidebar.radio('Page Navigation', ['page 1', 'page 2'])

if my_page == 'page 1':
#    st.title('here is a page')
#    button = st.button('a button')
#    if button:
#        st.write('clicked')
#else:
#    st.title('this is a different page')
#    slide = st.slider('this is a slider')
#    slide

    st.set_page_config(layout="wide")

    col1, col2 = st.columns([3, 8])
    # data = np.random.randn(10, 1)

    # col1.subheader("A wide column with a chart")
    # col1.line_chart(data)

    # col2.subheader("A narrow column with the data")
    # col2.write(data)

    url = 'https://yt3.ggpht.com/ytc/AKedOLQVlr4iXZKPReRK2U5gSs_KknhuA4iDmhas5N0Z=s900-c-k-c0x00ffffff-no-rj'
    logo = Image.open(requests.get(url, stream=True).raw)

    # header
    with col1:
        st.image(logo, width=100)
        st.header("NYC Tech Ecosystem")
        st.write("This view provides an overview of the NYC Tech Ecosystem representing 17 different sectors..Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusm magna aliqua. Ut enim ad minim veniam, quis nostrud.")
        st.button('Home')
        st.button('Ecosystem Overview')
        st.button('Sector Profile')

    with col2:
        # call to render Folium map in Streamlit
        folium_static(map)

        # table
        st.dataframe(df)



