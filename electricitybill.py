import pdfplumber
import pandas as pd

# Path to the PDF file
pdf_path = 'C:\\Users\\HP\\Downloads\\electricity_bill_aug24.pdf'

# List to store all DataFrames
dfs = []

# Open the PDF
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        # Extract table from each page
        tables = page.extract_tables()
        if tables:
            for table in tables:
                # Convert table to DataFrame and append to the list
                df = pd.DataFrame(table[1:], columns=table[0])  # First row as header
                dfs.append(df)

# Combine all extracted tables into a single DataFrame if needed
final_df = pd.concat(dfs, ignore_index=True)

# Display the final DataFrame
print(final_df)

# Optionally save to CSV or Excel
final_df.to_csv('output.csv', index=False)
final_df.to_excel('output.xlsx', index=False)
