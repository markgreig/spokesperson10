#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from collections import Counter
import pandas as pd
import re
import streamlit as st

spokesperson_data = Counter()
data = st.text_input("Paste text here")

for item in data:
    parts = item.split('|')
    for part in parts:
        words = part.split()
        name = " ".join(words[:-1])  # Join all words except the last one
        frequency = int(words[-1])
        spokesperson_data[name] += frequency

# Step 2: Create a DataFrame for the table
df = pd.DataFrame(list(spokesperson_data.items()), columns=["Spokesperson", "Frequency"])

# Step 3: Create the CSV table
st.write("CSV Table:")
st.dataframe(df)

# Step 4: Generate and download the CSV file
csv_file = df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv_file.encode(),
    key="download-button",
    file_name="spokesperson_frequency.csv",
    mime="text/csv",
)
