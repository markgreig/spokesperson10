#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import io
import streamlit as st
import pandas as pd

st.title("Generate Spokesperson Frequency CSV")

# Get text input
text = st.text_input("Paste data here")

# Convert text to DataFrame
df = pd.read_csv(io.StringIO(text))

# Split all rows on '|'  
df = df.apply(lambda x: x.str.split('|').explode()).reset_index(drop=True)

# Keep only 'Spokesperson' column
df = df['Spokesperson']  

# Group by spokesperson and count frequencies
df = df.groupby(df.columns[0], as_index=False)[df.columns[0]].count().rename(columns={df.columns[0]: "Frequency"})

# Display dataframe preview
st.dataframe(df)

# Download CSV file 
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    "Press to Download",
    csv,
    "spokesperson_frequency.csv",
    "text/csv",
    key='download-csv'
)

