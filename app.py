import streamlit as st
import pandas as pd
import numpy as np
import streamlit_pandas as sp
import glob

st.set_page_config(layout="wide")
st.title('KSR - Militarization of Police')

file = "202304-Equipment-List.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df


df = load_data()

category_list = list(df['Category'].unique())

category = st.selectbox(label="Choose a category", options=category_list)
name = st.text_input(label="Search up military equipment by name")

image_files = df['Link to image'].tolist()
caption_list = df['Listed Name'].tolist()

n = 4
groups = []
caption_groups = []
for i in range(0, len(image_files), n):
    groups.append(image_files[i:i+n])
    caption_groups.append(caption_list[i:i+n])

cols = st.columns(n)
r = 0
for group in groups:
    for i, img in enumerate(group):
        cols[i].image(img, use_column_width=True, caption=caption_groups[r][i])
    r += 1


filtered_images = []


load_images()

# st.write(df)

# create_data = {
#                 "Category" : "select"
#               }

# all_widgets = sp.create_widgets(df, create_data, ignore_columns=["Category Description"])
# res = sp.filter_df(df, all_widgets)
# st.write(res)
