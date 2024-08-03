import re

def title_type_change():
    """Turn tsx file from imdb to csv file."""
    input_file_path = "data/extracted/title.basics.tsv"
    output_file_path = "data/extracted/imdb_title.csv"

    try:
        with open(input_file_path, 'r', encoding='utf-8') as tsv_file:
            with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                for line in tsv_file:
                    csv_content = re.sub("\t", ",", line)
                    
                    # Write the content to the CSV file
                    csv_file.write(csv_content)
                    
        print(f"CSV file '{output_file_path}' created successfully.")
    
    except UnicodeDecodeError:
        print("Error: The file contains characters that could not be decoded using 'utf-8' encoding.")
        print("Trying with a different encoding...")

        try:
            with open(input_file_path, 'r', encoding='latin1') as tsv_file:
                with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                    for line in tsv_file:
                        csv_content = re.sub("\t", ",", line)
                        csv_file.write(csv_content)
                        
            print(f"CSV file '{output_file_path}' created successfully with 'latin1' encoding.")
        
        except Exception as e:
            print(f"Failed to create CSV file: {e}")

def ratings_type_change():
    """Turn tsx file from imdb to csv file."""
    input_file_path = "data/extracted/title.ratings.tsv"
    output_file_path = "data/extracted/ratings.csv"

    try:
        with open(input_file_path, 'r', encoding='utf-8') as tsv_file:
            with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                for line in tsv_file:
                    csv_content = re.sub("\t", ",", line)
                    
                    # Write the content to the CSV file
                    csv_file.write(csv_content)
                    
        print(f"CSV file '{output_file_path}' created successfully.")
    
    except UnicodeDecodeError:
        print("Error: The file contains characters that could not be decoded using 'utf-8' encoding.")
        print("Trying with a different encoding...")

        try:
            with open(input_file_path, 'r', encoding='latin1') as tsv_file:
                with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                    for line in tsv_file:
                        csv_content = re.sub("\t", ",", line)
                        csv_file.write(csv_content)
                        
            print(f"CSV file '{output_file_path}' created successfully with 'latin1' encoding.")
        
        except Exception as e:
            print(f"Failed to create CSV file: {e}")

def language_type_change():
    """Turn tsx file from imdb to csv file."""
    input_file_path = "data/extracted/title.akas.tsv"
    output_file_path = "data/extracted/language.csv"

    try:
        with open(input_file_path, 'r', encoding='utf-8') as tsv_file:
            with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                for line in tsv_file:
                    csv_content = re.sub("\t", ",", line)
                    
                    # Write the content to the CSV file
                    csv_file.write(csv_content)
                    
        print(f"CSV file '{output_file_path}' created successfully.")
    
    except UnicodeDecodeError:
        print("Error: The file contains characters that could not be decoded using 'utf-8' encoding.")
        print("Trying with a different encoding...")

        try:
            with open(input_file_path, 'r', encoding='latin1') as tsv_file:
                with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                    for line in tsv_file:
                        csv_content = re.sub("\t", ",", line)
                        csv_file.write(csv_content)
                        
            print(f"CSV file '{output_file_path}' created successfully with 'latin1' encoding.")
        
        except Exception as e:
            print(f"Failed to create CSV file: {e}")
