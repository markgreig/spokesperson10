#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import re
import streamlit as st
import pandas as pd

@st.cache
def process_data(text):
    # Extract rows
    rows = re.findall(r'\"?([^"]+)\"?\s(\d+)', text)

    # Split spokesperson column and create data list
    data = []
    for row in rows:
        spokespersons = [name.strip() for name in row[0].strip().split('|')]
        frequency = int(row[1])
        for spokesperson in spokespersons:
            data.append([spokesperson, frequency])

    # Create dataframe  
    df = pd.DataFrame(data, columns=['Spokesperson', 'Frequency'])

    # Group by Spokesperson and calculate the sum of Frequency
    result = df.groupby('Spokesperson')['Frequency'].sum().reset_index()

    # Sort by Frequency in descending order
    result = result.sort_values(by='Frequency', ascending=False)

    return result

def main():
    st.title('My App') 

    text = st.text_input("Paste text here")

    if text:
        result = process_data(text)

        st.write(result)

        csv = result.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='top_spokespeople.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
