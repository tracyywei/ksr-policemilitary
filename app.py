import streamlit as st
import pandas as pd
import numpy as np
import streamlit_pandas as sp
import glob

st.set_page_config(layout="wide")
st.title('What makes up military equipment inventory?')
st.subheader('Made by the Know System Racism Project')

@st.cache_data
def load_data():
    df = pd.read_csv("data/202304-Equipment-List.csv")
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
company_list = ["None"]
for i in list(reformated['Manufacturer'].unique()) :
    company_list.append(i)
category = st.multiselect(label="Choose a category", options=category_list)
name = st.text_input(label="Search up military equipment by name")
company = st.selectbox(label="Select a manufacturer", options=company_list)
c_list = df['Category'].tolist()

def path_to_image_html(path):
    return '<img src="' + path + '" width="100" >'

def convert_df(input_df):
     return input_df.to_html(escape=False, formatters=dict(Image=path_to_image_html))

def filter_table():
    filtered_entries = pd.DataFrame()

    # filter by selected category and search by name
    for cat in category :
        for x in range(0, len(c_list)):
            if c_list[x] == cat and name in reformated.iloc[x]['Listed Name']:
                if company == "None":
                    filtered_entries = filtered_entries.append(reformated.iloc[x])
                elif company == reformated.iloc[x]['Manufacturer']:
                    filtered_entries = filtered_entries.append(reformated.iloc[x])

    
    html = convert_df(filtered_entries)
   
    st.markdown(
        html,
        unsafe_allow_html=True
    )

if category == [] :
   html = convert_df(reformated)
   st.markdown(
    html,
    unsafe_allow_html=True
    )
else : 
    filter_table()
