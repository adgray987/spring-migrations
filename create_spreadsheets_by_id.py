#!/usr/bin/env python
# coding: utf-8

# Disaggregate a Spreadsheet by Collection ID
# Use collection identifiers in a specified column to create separate Excel spreadsheets (.xlsx) for every collection identifier and its corresponding row(s).
# 
# Requirements:
# - Pandas
# - Tabular data with a column for a collection identier. Identfier column could be EADID, collection name, accession number, etc.

# Set up environment
import pandas as pd
import numpy as np


# Load file and create DataFrame. Modify file path and header argument as needed.
file = "path to your file"
records = pd.read_excel(file)

# Specify column with the identifiers
id_column = "name of your id column"



# Check the shape of the DataFrame (rows x columns)
print(f'There are a total of {records.shape[0]} rows and {records.shape[1]} columns')

# View null counts and dtypes for all columns
records.info()



# Put all IDs into a sorted list
ids =[]
for row in records[id_column].unique():
    ids.append(row)
#ids.sort()
print(ids[0:10])

print(f"{len(ids)} unique ids")



# Create individual spreasheets for every group of rows correspondeing to the IDs
# Length of list of ids will equal the number of spreadsheets
# .dropna() method will remove empty columns; different spreadsheets will have different columns
# depending on which columns are empty for that ID
for i in ids:
    df = records[records[id_column] == i].dropna(axis=1, how="all")
    # Change file path below as needed
    df.to_excel(f"{i}.xlsx")