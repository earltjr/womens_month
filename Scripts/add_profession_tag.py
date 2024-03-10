import pandas as pd
import glob
from profession_tag import tag_prefixes
import os


#function that checks a string to see if it has substrings that match the professions_tag variable
def find_tags(text, tag_prefixes):
    # Check if the input text is a string
    if not isinstance(text, str):
        print("Input is not a string.")
        return []

    # Lowercase the entire tag_prefixes dictionary
    lowercase_tag_prefixes = {tag: [prefix.lower() for prefix in prefixes] for tag, prefixes in tag_prefixes.items()}
    
    # Find tags based on lowercased tag prefixes
    matched_tags = [tag for tag in lowercase_tag_prefixes if any(prefix in text.lower() for prefix in lowercase_tag_prefixes[tag])]
    
    return matched_tags


# Specify input and output folder where input folder is where the file of interest is and the output where the modified file will go
input_folder = "C:/Users/Earl/Documents/womens_month/step3_professions_added"
output_folder="C:/Users/Earl/Documents/womens_month/step4_profession_tags_added"

for xlsx_file_path in glob.glob(input_folder + "/*.xlsx"):
    # Load Excel data into a DataFrame
    df = pd.read_excel(xlsx_file_path)
    base_filename = os.path.basename(xlsx_file_path)
    
    
    # Create a new "Tags" column in the DataFrame
    df["Tags"] = ""

    # Output the predicted profession tags
    for index, row in df.iterrows():
        cell_text = str(row["Notes"])

        matched_tags = find_tags(cell_text, tag_prefixes)
       
        if matched_tags:
            df.at[index, "Tags"] = ", ".join(matched_tags)
        else:
            df.at[index, "Tags"] = "other"

    output_excel_path = os.path.join(output_folder, f"{base_filename[:-5]}-tags_added.xlsx")
    df.to_excel(output_excel_path, index=False)
    print(f"Processed: {base_filename}")

print("All Excel files processed.")
