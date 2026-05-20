import os
from pathlib import Path
from dotenv import load_dotenv

def setup_spotify_api_env():
    env_path = Path('.') / '.env'
    print(f"Checking for Spotify credentials in: {env_path.resolve()}")

    # Check if .env file exists
    if not env_path.exists():
        print(".env file not found!")
        print("Please follow the steps below to set it up:")
        print("1. Go to the Spotify Developer Dashboard and log in: https://developer.spotify.com/dashboard/")
        print("2. Create an app to get your Client ID and Client Secret")
        print("3. In the project folder, create a file named `.env`")
        print("4. Add the following lines to your `.env` file:")
        print("   SPOTIPY_CLIENT_ID=your_client_id_here")
        print("   SPOTIPY_CLIENT_SECRET=your_client_secret_here")
        input("Press Enter after you've created the .env file and added your credentials")
        if not env_path.exists():
            print(".env file still not found. Please try again")
            return

    # Load and check client id and secret from .env file
    load_dotenv(dotenv_path=env_path)

    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("One or both Spotify credentials are missing in your .env file")
        print("Please make sure your .env file includes both lines:")
        print("   SPOTIPY_CLIENT_ID=your_client_id_here")
        print("   SPOTIPY_CLIENT_SECRET=your_client_secret_here")
        return

    # Confirm success
    print("Spotify API credentials are set up correctly.")
    print(f"Client ID: {client_id[:4]}****")
    print(f"Client Secret: {client_secret[:4]}****")

setup_spotify_api_env()
