import streamlit as st
import pandas as pd
import numpy as np
import streamlit_pandas as sp
import glob

st.set_page_config(layout="wide")
st.title('Table View')

file = "202304-Equipment-List.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

df = load_data()

image_files = df['Link to image'].tolist()
name_list = df['Listed Name'].tolist()

reformated = pd.DataFrame()
reformated["Image"] = image_files
reformated["Listed Name"] = name_list
reformated["Cost"] = df['Cost'].tolist()
reformated["Life Span (years)"] = df["Life Span (years)"].tolist()
reformated["Category"] = df['Category'].tolist()
reformated["Category Description"] = df['Category Description'].tolist()
reformated["Manufacturer"] = df['Manufacturer'].tolist()

category_list = list(reformated['Category'].unique())
category = st.selectbox(label="Choose a category", options=category_list)
name = st.text_input(label="Search up military equipment by name")

def path_to_image_html(path):
    return '<img src="' + path + '" width="100" >'

def convert_df(input_df):
     return input_df.to_html(escape=False, formatters=dict(Image=path_to_image_html))

html = convert_df(reformated)
st.markdown(
    html,
    unsafe_allow_html=True
)