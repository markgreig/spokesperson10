#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st
import pandas as pd

# Example data
data = st.text_input("Paste text here")

# Function to split and group spokespeople
def process_data(data):
    rows = data.split("\n")
    processed_data = []
    for row in rows:
        spokespeople = row.split("|")
        for spokesperson in spokespeople:
            processed_data.append([spokesperson.strip(), 1])
    df = pd.DataFrame(processed_data, columns=["Spokesperson", "Frequency"])
    df = df.groupby("Spokesperson").sum().reset_index()
    return df

# Streamlit app
def main():
    st.title("Spokesperson Frequency")
    st.write("Preview of the CSV file:")

    # Process the data
    df = process_data(data)

    # Show the preview table
    st.write(df)

    # Download link for the CSV file
    csv = df.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name="spokesperson_frequency.csv")

if __name__ == "__main__":
    main()
