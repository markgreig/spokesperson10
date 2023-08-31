#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st
import csv

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
    # Specify the output file name
    output_file = 'output.csv'
    
    # Open the file in write mode
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Spokesperson', 'Frequency'])
        
        # Write the data rows
        for spokesperson, frequency in frequencies.items():
            writer.writerow([spokesperson, frequency])
    
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


