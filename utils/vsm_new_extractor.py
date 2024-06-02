import pdfplumber
import pandas as pd

# Open the PDF file
with pdfplumber.open('vsm_2023_4_2024_1_modositott.pdf') as pdf:
    # Initialize an empty list to store the tables from each page
    all_tables = []
    
    # Iterate over each page in the PDF
    for page in pdf.pages:
        # Extract the table
        table = page.extract_table()
        
        # Remove the unnecessary rows
        table = table[2:]
        
        # Append the table to the list
        all_tables.append(table)
    
    # Concatenate all the tables into one DataFrame
    df = pd.concat([pd.DataFrame(table, columns=table[0]) for table in all_tables], ignore_index=True) # type: ignore

    # Remove all rows that contain the text 'Azon.'
    df = df[~df.apply(lambda row: row.astype(str).str.contains('Azon.').any(), axis=1)]


# Set the first column as the index
df.set_index(df.columns[0], inplace=True)
df.index.name = "sorszam"

dates = df.columns.tolist()[2:4]
df.columns = ["kepzo_nev", "kepzo_azonosito", f"AM_elm_{dates[0]}", f"AM_elm_{dates[1]}", f"AM_forg_{dates[0]}", f"AM_forg_{dates[1]}", f"A1A2Asum_elm_{dates[0]}", f"A1A2Asum_elm_{dates[1]}", f"A1A2Asum_forg_{dates[0]}", f"A1A2Asum_forg_{dates[1]}", f"B_elm_{dates[0]}", f"B_elm_{dates[1]}", f"B_forg_{dates[0]}", f"B_forg_{dates[1]}", f"C_elm_{dates[0]}", f"C_elm_{dates[1]}", f"C_forg_{dates[0]}", f"C_forg_{dates[1]}"]

print(df)

# Save the DataFrame to a CSV file
df.to_csv('vsm_data.csv')