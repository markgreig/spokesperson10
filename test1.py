#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import io
import streamlit as st
import pandas as pd

st.title("Generate Spokesperson Frequency CSV") 

# Get text input
text = st.text_input("Paste data here")

# Validate input
if not text:
    st.error("Please enter valid CSV data")
else:
    # Convert text to DataFrame
    try:
        df = pd.read_csv(io.StringIO(text)) 
    except Exception as e:
        st.error("Error parsing input data")

    # Split rows on '|'
    df = df.apply(lambda x: x.str.split('|').explode()).reset_index(drop=True)
    
    # Check number of columns
    if len(df.columns) == 1:
        # Use unnamed column
        df = df[df.columns[0]] 
    else:
        # Rename column to 'Spokesperson'
        df = df.rename(columns={df.columns[0]: 'Spokesperson'})
        
    # Group and count frequencies
    df = df.groupby(df.columns[0], as_index=False)[df.columns[0]].count().rename(columns={df.columns[0]: "Frequency"})

    # Display preview
    st.dataframe(df)

    # Download CSV
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
