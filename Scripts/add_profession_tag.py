import pandas as pd
import spacy
import glob
from profession_tag import tag_prefixes
import os
# figure out how to use tag_prefixes
#professions=list(set(professions))
# Load language model
nlp = spacy.load("en_core_web_lg")

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


# Specify for partially cleaned CSV files
folderpath = "C:/Users/Earl/Documents/Womens month cvs/partially-manually cleaned"
for csv_file_path in glob.glob(folderpath + "/*.csv"):
    
    # Load CSV data into a DataFrame
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
    base_filename=os.path.basename(csv_file_path)
    print(base_filename)
    
    # Create a new "Tags" column in the DataFrame
    df["Tags"] = ""

     # Output the predicted profession tags
    for index, row in df.iterrows():
        
     cell_text=str(row["Notes"])

     matched_tags= find_tags(cell_text,tag_prefixes)
     print("matched tags are:"+str(matched_tags))
     if matched_tags:
        df.at[index,"Tags"]=", ".join(matched_tags)
     else:
        df.at[index,"Tags"]="other"
    output_csv_path = f"{folderpath}/{base_filename}" 
    df.to_csv(output_csv_path, index=False)
    print(f"Processed: {csv_file_path}, Output CSV: {output_csv_path}")    
print("All CSV files processed.")

# for file in input_folder
#  df= file 
#     for every cell in df
#    check if cell contain any prefixes 
#     if yes return that return the name of that dictionary do not add again for every isinstance
#     next cell
#  save file in output_folder as same name