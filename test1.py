#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import streamlit as st
from io import StringIO

data = st.text_input("Paste text here")

# Read the data into a pandas DataFrame
df = pd.read_csv(StringIO(data), sep='\t')

# Expand the DataFrame to create a new row for each spokesperson in rows with multiple spokespeople
df = df.assign(Spokesperson=df['Spokesperson'].str.split('|')).explode('Spokesperson')

# Group by 'Spokesperson' and sum the 'Frequency'
df = df.groupby('Spokesperson', as_index=False).sum()

# Display the DataFrame in Streamlit
st.dataframe(df)

# Write the DataFrame to a CSV file and provide a download link in Streamlit
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings
linko= f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download csv file</a>'
st.markdown(linko, unsafe_allow_html=True)
