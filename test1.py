#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st
import pandas as pd

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
    
    # Specify the output file name
    output_file = 'output.csv'
    
    # Save the DataFrame as a CSV file
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
        st.success(f'CSV file "{output_file}" generated successfully.')
        
        # Download link for the CSV file
        st.markdown(f"Download the CSV file: [output.csv](./{output_file})")

if __name__ == '__main__':
    main()
