import pandas as pd
import glob
from professions import professions
import os
import openpyxl

#checks list for duplicates before using as list variable
professions=list(set(professions))


# Function to find profession using input text and comparing to professions variable
def find_professions(text, professions):
    return [prof for prof in professions if prof.lower() in text.lower()]

# Specify input folder containing excel files
input_folder = "C:/Users/Earl/Documents/womens_month/step2_cvs_to_xlsx"

# Specify output folder for cleaned excel files
output_folder = "C:/Users/Earl/Documents/womens_month/step3_professions_added"

# Iterate through all excel files in the input folder
for xlsx_file_path in glob.glob(input_folder + "/*.xlsx"):
    # Load excel data into a DataFrame
    df = pd.read_excel(xlsx_file_path)

    #find base file name
    base_filename=os.path.basename(xlsx_file_path)
   
    # Output the predicted profession(s)
    for index, row in df.iterrows():

        # Get the text from Notes column
        cell_text = str(row["Notes"])

        #Find professions in the cell text
        matched_professions = find_professions(cell_text, professions)

        # Write the matched professions to column C
        if matched_professions:
            df.at[index, "Field(s)"] = ", ".join(matched_professions)
        else:
            df.at[index, "Field(s)"] = "Other"

    # Save the updated DataFrame to a new excel file in the output folder
    output_excel_path = os.path.join(output_folder, f"{base_filename[:-5]}-profs_added.xlsx")

    df.to_excel(output_excel_path, index=False)
    print(f"Processed: {base_filename}")

print("All Excel files processed.")
