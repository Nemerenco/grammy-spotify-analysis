from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

dataset = 'unanimad/grammy-awards'
download_path = './data/'

# Download the dataset
api.dataset_download_files(dataset, path=download_path, unzip=True)

# List the files
extracted_files = os.listdir(download_path)
print("Extracted files:", extracted_files)
