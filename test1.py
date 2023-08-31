#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st
import pandas as pd
import base64

# Get the data from the text input field
text = st.text_input("Paste text here")

# Split the text into lines and extract the data
lines = text.split("\n")
data = []
for line in lines:
    parts = line.split()
    frequency = int(parts[-1])
    spokesperson = " ".join(parts[:-1])
    data.append([spokesperson, frequency])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=["Spokesperson", "Frequency"])

# Split out the rows with multiple spokespeople separated by the pipe symbol
df = df.assign(Spokesperson=df["Spokesperson"].str.split("|")).explode("Spokesperson")

# Group the spokespeople so that only distinct spokespeople are left
df = df.groupby("Spokesperson").sum().reset_index()

# Preview the output in Streamlit
st.write(df)

# Download the CSV file
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="spokespeople.csv">Download CSV File</a>'
st.markdown(href, unsafe_allow_html=True)

