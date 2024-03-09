import pandas as pd
import os
import glob
import unicodedata

def remove_non_alpha(text):
    # Check if the input is a string
    if not isinstance(text, str):
        return ""

    # Normalize the text to NFKD form to handle accented characters
    normalized_text = unicodedata.normalize('NFKD', text)

    # Use translate to remove non-alphabetic characters
    clean_text = normalized_text.encode('ascii', 'ignore').decode('utf-8')
    
    return clean_text

# Specify input folder containing CSV files
folderpath = "C:/Users/Earl/Documents/Womens month cvs/uncleaned"

# Specify output folder for cleaned CSV files
output_folder = "C:/Users/Earl/Documents/Womens month cvs/cleaned"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all CSV files in the input folder
for csv_file_path in glob.glob(folderpath + "/*.csv"):
    # Load CSV data into a DataFrame
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

    # Apply the cleaning function to the relevant column (e.g., "Notes")
    df["Cleaned_Notes"] = df["Notes"].apply(remove_non_alpha)

    # Save the cleaned DataFrame to a new CSV file in the output folder
    base_filename = os.path.basename(csv_file_path)
    output_csv_path = os.path.join(output_folder, f"{base_filename[:-4]}-cleaned.csv")
    df.to_csv(output_csv_path, index=False)

    print(f"Processed: {csv_file_path}, Output CSV: {output_csv_path}")

print("All CSV files processed.")
