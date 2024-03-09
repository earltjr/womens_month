import pandas as pd
import glob
from professions import professions
import os


professions=list(set(professions))


# Function to find profession using input text and comparing to professions variable
def find_professions(text, professions):
    return [prof for prof in professions if prof.lower() in text.lower()]

# Specify input folder containing CSV files
input_folder = "C:/Users/Earl/Documents/Womens month cvs/uncleaned"

# Specify output folder for cleaned CSV files
output_folder = "C:/Users/Earl/Documents/Womens month cvs/partially-manually cleaned"

# Iterate through all CSV files in the input folder
for csv_file_path in glob.glob(input_folder + "/*.csv"):
    # Load CSV data into a DataFrame
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
    base_filename=os.path.basename(csv_file_path)
    print(base_filename)
    
    # Output the predicted profession(s)
    for index, row in df.iterrows():
        # Get the text from column D
        cell_text = str(row["Notes"])

        # Find professions in the cell text
        matched_professions = find_professions(cell_text, professions)

        # Write the matched professions to column C
        if matched_professions:
            df.at[index, "Field(s)"] = ", ".join(matched_professions)
        else:
            df.at[index, "Field(s)"] = "Other"

    # Save the updated DataFrame to a new CSV file in the output folder
    output_csv_path = os.path.join(output_folder, f"{base_filename[:-4]}-partially_cleaned.csv")

    df.to_csv(output_csv_path, index=False)
    print(f"Processed: {csv_file_path}, Output CSV: {output_csv_path}")

print("All CSV files processed.")
