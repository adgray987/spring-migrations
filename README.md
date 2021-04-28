# Migration Toolkit
Notebooks and scripts I've used in various projects for migrating legacy collections data.

# What's here

## create_spreadsheets_by_id 
Uses collection identifiers in a specified column to create separate Excel spreadsheets (.xlsx) for every collection identifier and its corresponding row(s).
- Requirements:
    - Pandas
    - Tabular data with a column for a collection identier. Identfier column could be EADID, collection name, accession number, etc.
