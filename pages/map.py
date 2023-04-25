import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
from plotly.subplots import make_subplots
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import threading

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

# Define a callback function to handle clicks on markers
def on_selected(trace, points, selector):
    selected_name = trace.hovertext[points.point_inds[0]]
    print(f"Selected name: {selected_name}")

# Initialize the state variable
state = {"selected_name": None}

fig = go.Figure()

fig.add_trace(
    go.Choroplethmapbox(
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
)

fig.add_trace(
    go.Scattermapbox(
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
)

# Set the on_click event handler for the scattermapbox trace
fig.data[1].on_selection(on_selected)

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=5,
    mapbox_center={"lat": 37, "lon": -120},
    width=800,
    height=600,
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    clickmode='event+select'
)

st.plotly_chart(fig)

# Access the selected name from the state variable
selected_name = state["selected_name"]
print(f"Selected name: {selected_name}")


# Define the data table
def load_lea_data():
    df = pd.read_csv("data/lea_list.csv")
    df['County'] = df['County'].str.replace(' County', '')
    return df

lea_df = load_lea_data()
filtered_data = lea_df 


# # Add an event handler for the plotly_click event
# def on_click(trace, points, state):
#     global filtered_data
#     console.log("HIIII")
#     if points.marker.color[0]:
#         clicked_county = points.customdata[0]  # get the clicked county name
#         filtered_data = lea_df[lea_df['County'] == clicked_county]
#         table = st.table(filtered_data)


table = st.table(filtered_data)

# # Bind the event handler to the click event
# fig.data[0].on_click(on_click)