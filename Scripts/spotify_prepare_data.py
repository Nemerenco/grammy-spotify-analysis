import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Load environment variables
load_dotenv()

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load Grammy dataset
grammy_df = pd.read_csv('data/the_grammy_awards.csv')

# Clean artist column and get unique names
artist_names = grammy_df['artist'].dropna().unique()

# Count Grammy wins per artist
grammy_wins = (
    grammy_df[grammy_df['winner'] == True]
    .groupby('artist')
    .size()  # Count how many times each artist has a "True" value
    .reset_index(name='Grammy Wins')
)

# Prepare list to hold Spotify data
spotify_data = []

for name in artist_names:
    try:
        results = sp.search(q=f"artist:{name}", type="artist", limit=1)
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            spotify_data.append({
                'Artist': artist['name'],
                'Followers': artist['followers']['total'],
                'Genres': ', '.join(artist['genres']),
                'Spotify URL': artist['external_urls']['spotify']
            })
    except Exception as e:
        print(f"Error fetching {name}: {e}")

# Convert Spotify results to DataFrame
spotify_df = pd.DataFrame(spotify_data)

# Clean Spotify data
spotify_df.dropna(subset=['Followers'], inplace=True)
spotify_df.drop_duplicates(subset='Artist', inplace=True)

# Merge with Grammy wins on artist name
grammy_wins.rename(columns={'artist': 'Artist'}, inplace=True)
final_df = spotify_df.merge(
    grammy_wins,
    how='right',
    on='Artist'
)

# Sort by followers, descending
final_df.sort_values(by='Followers', ascending=False, inplace=True)
final_df.reset_index(drop=True, inplace=True)

# Save to CSV
output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'spotify_grammy_artist_data.csv')
final_df.to_csv(output_path, index=False)
