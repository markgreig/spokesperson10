#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st
import pandas as pd
from io import BytesIO

def process_data(input_data):
    # Split the input data into lines
    lines = input_data.strip().split('\n')
    
    # Create a dictionary to store the frequencies of spokespeople
    frequencies = {}
    
    # Iterate over each line and extract the spokespeople
    for line in lines:
        # Split the line into columns
        columns = line.split('\t')
        
        # Extract the spokespeople from the second column
        spokespeople = columns[1].split('|')
        
        # Update the frequencies dictionary
        for spokesperson in spokespeople:
            frequencies[spokesperson] = frequencies.get(spokesperson, 0) + 1
    
    return frequencies

def generate_csv(frequencies):
    # Create a DataFrame from the frequencies dictionary
    df = pd.DataFrame(frequencies.items(), columns=['Spokesperson', 'Frequency'])
    
    # Create a file-like object in memory
    output_file = BytesIO()
    
    # Save the DataFrame as a CSV file in the file-like object
    df.to_csv(output_file, index=False)
    
    return output_file

# Streamlit app
def main():
    st.title("Spokespeople Frequency Counter")
    
    # Text input for the data
    input_data = st.text_area("Paste the data here:")
    
    # Process the data and generate the CSV file
    if st.button("Generate CSV"):
        frequencies = process_data(input_data)
        output_file = generate_csv(frequencies)
        st.success('CSV file generated successfully.')
        
        # Download link for the CSV file
        st.markdown(get_download_link(output_file, 'output.csv'), unsafe_allow_html=True)

def get_download_link(file, file_name):
    # Convert the file-like object to bytes
    file_bytes = file.getvalue()
    
    # Generate a download link for the file
    href = f'<a href="data:file/csv;base64,{file_bytes.decode()}" download="{file_name}">Download CSV file</a>'
    
    return href

if __name__ == '__main__':
    main()
