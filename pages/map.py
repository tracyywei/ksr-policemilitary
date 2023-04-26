import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
from plotly.subplots import make_subplots
from streamlit_plotly_events import plotly_events

import os
# checking that the current working directory is correct to ensure that the file paths are working
if os.getcwd()[-3:] == "src":
    os.chdir('..')

@st.cache_data

# LOAD DATAFRAME FUNCTION
def load_data(path):
    df = pd.read_csv(path, encoding= 'latin1')
    df['name'] = df['name'].str.replace(' County', '')
    return df

# LOAD GEIJASON FILE
with open("data/California_County_Boundaries.geojson") as response:
    geo = json.load(response)

df = load_data("data/ca_population.csv")

leas = pd.read_csv("data/LEA-20230424.csv")

# Geographic Map
st.title("Map: Military Equipment Inventory in Law Enforcement Agencies")

fig = go.Figure()

choro_trace = go.Choroplethmapbox(
        geojson=geo,
        locations=df.name,
        featureidkey="properties.COUNTY_NAME",
        z=df.pop2023,
        colorscale="sunsetdark",
        marker_opacity=0.6,
        marker_line_width=1,
        hovertemplate="<b>%{location} County</b><br>Population: %{z:,}",
        customdata=df.name
    )

scatter_trace = go.Scattermapbox(
        lat = leas['Latitude'],
        lon = leas['Longitude'],
        mode="markers",
        marker=go.scattermapbox.Marker(
            size=5,
            color="red"
        ),
        hovertemplate=leas['LEA_Name'],
        selected={
            "marker": {
                "color": "blue",
                "size": 15
            }
        }
    )

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=5,
    mapbox_center={"lat": 37, "lon": -120},
    width=800,
    height=800,
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    clickmode='event+select'
)

fig.add_trace(choro_trace)
fig.add_trace(scatter_trace)

selected_points = plotly_events(fig)
selected_lea = ""
for point in selected_points :
    index = point['pointIndex']
    leaID = leas.iloc[index]['Ref']
    selected_lea = leaID


# Define the data table
def load_lea_data():
    df = pd.read_csv("data/lea_list.csv")
    df['County'] = df['County'].str.replace(' County', '')
    return df

lea_df = load_lea_data()

def filter_table():
    filtered_entries = lea_df[lea_df['Ref'] == selected_lea]
    return filtered_entries

filtered_df = filter_table()
if(not filtered_df.empty) :
    st.header(filtered_df['LEA_Name'])
    table = st.table(filtered_df)
