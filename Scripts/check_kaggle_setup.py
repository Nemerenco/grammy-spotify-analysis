import os
from pathlib import Path

def setup_kaggle_api_key():
    # Define the location where Kaggle expects the API key
    kaggle_dir = Path.home() / '.kaggle'
    print(f"Checking for Kaggle API key in: {kaggle_dir}")

    # Check if the '.kaggle' directory exists, if not, create it
    if not kaggle_dir.exists():
        print("Creating the '.kaggle' directory...")
        kaggle_dir.mkdir(parents=True, exist_ok=True)

    # Check if the API key file exists
    kaggle_json_path = kaggle_dir / 'kaggle.json'
    if kaggle_json_path.exists():
        print("Kaggle API key is already set up")
        print(f"Your Kaggle API key is located at: {kaggle_json_path}")
        return

    # If the API key is not found, guide the user to download the kaggle.json file
    print("Kaggle API key not found!")
    print("Please follow the steps to set it up:")
    print("1. Go to your Kaggle account page: https://www.kaggle.com/settings")
    print("2. Scroll to the 'API' section and click 'Create New API Token'")
    print("3. A file named 'kaggle.json' will be downloaded")
    print(f"4. Upload the kaggle.json file in: {kaggle_json_path}")
    input("Press Enter after you have placed kaggle.json in the correct directory")

    # Check if the file was placed correctly
    if os.path.exists(kaggle_json_path):
        print(f"Kaggle API key is successfully set up at: {kaggle_json_path}")
    else:
        print("The 'kaggle.json' file was not found. Please try again")

setup_kaggle_api_key()