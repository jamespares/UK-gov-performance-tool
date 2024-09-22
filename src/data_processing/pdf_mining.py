# src/data_processing/pdf_mining.py

import pdfplumber
import pandas as pd

def extract_table_from_pdf(pdf_path):
    """
    Extract tables from the given PDF and return as a DataFrame.
    :param pdf_path: Path to the PDF file.
    """
    with pdfplumber.open(pdf_path) as pdf:
        all_tables = []
        for page in pdf.pages:
            # Extract tables from each page
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                all_tables.append(df)

        # Combine all extracted tables into one DataFrame
        combined_df = pd.concat(all_tables, ignore_index=True)
        return combined_df

# Example usage
pdf_path = "downloaded_pdfs/annual_report_2023.pdf"
df = extract_table_from_pdf(pdf_path)
print(df.head())