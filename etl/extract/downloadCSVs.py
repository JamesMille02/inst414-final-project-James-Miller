import os
import requests
import gzip
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

# Function to download a file from a URL
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded successfully and saved to {save_path}")
    else:
        print(f"Failed to download file. HTTP status code: {response.status_code}")

# Function to extract .gz files
def extract_gz(file_path, output_path):
    with gzip.open(file_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"File extracted successfully and saved to {output_path}")

# Function to download IMDb datasets
def download_imdb_datasets():
    # Base URL for IMDb data files
    base_url = "https://datasets.imdbws.com/"

    # List of files to download
    files_to_download = [
        "title.basics.tsv.gz",
        "title.ratings.tsv.gz",
        "title.akas.tsv.gz"
    ]

    # Directory to save the downloaded files
    save_directory = os.path.join("data", "extracted")
    os.makedirs(save_directory, exist_ok=True)

    # Download and extract each file
    for file_name in files_to_download:
        gz_file_name = file_name
        tsv_file_name = file_name.replace('.gz', '')
        
        gz_file_path = os.path.join(save_directory, gz_file_name)
        tsv_file_path = os.path.join(save_directory, tsv_file_name)

        # Download the .gz file
        file_url = f"{base_url}{gz_file_name}"
        download_file(file_url, gz_file_path)

        # Extract the .gz file to .tsv
        extract_gz(gz_file_path, tsv_file_path)

        # Remove the .gz file if no longer needed
        os.remove(gz_file_path)

# Function to download Kaggle datasets
def download_kaggle_dataset(dataset, save_directory):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=save_directory, unzip=True)
    print(f"Kaggle dataset '{dataset}' downloaded and saved to {save_directory}")

def download_kaggle_datasets():
    # List of Kaggle datasets to download
    datasets_to_download = [
        "unanimad/the-oscar-award",
        "unanimad/golden-globe-awards"
    ]

    # Directory to save the downloaded files
    save_directory = os.path.join("data", "extracted")
    os.makedirs(save_directory, exist_ok=True)

    # Download each dataset
    for dataset in datasets_to_download:
        download_kaggle_dataset(dataset, save_directory)


