import streamlit as st
import pandas as pd
import numpy as np
import streamlit_pandas as sp
import glob

st.set_page_config(layout="wide")
st.title('Gallery View')

file = "data/202304-Equipment-List.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

df = load_data()

#########

category_list = list(df['Category'].unique())

category = st.selectbox(label="Choose a category", options=category_list)
name = st.text_input(label="Search up military equipment by name")

image_files = df['Link to image'].tolist()
name_list = df['Listed Name'].tolist()
category_list = df['Category'].tolist()

def filter_images():
    filtered_images = []
    filtered_names = []

    # filter by selected category and search by name
    for x in range(0, len(category_list)):
        if category_list[x] == category and name in name_list[x] :
            filtered_images.append(image_files[x])
            filtered_names.append(name_list[x])

    return filtered_images, filtered_names

def load_images():
    filtered_images, filtered_names = filter_images()
    n = 4
    groups = []
    caption_groups = []
    for i in range(0, len(filtered_images), n):
        groups.append(filtered_images[i:i+n])
        caption_groups.append(filtered_names[i:i+n])

    cols = st.columns(n)
    r = 0
    for group in groups:
        for i, img in enumerate(group):
            cols[i].image(img, use_column_width=True, caption=caption_groups[r][i])
        r += 1

load_images()