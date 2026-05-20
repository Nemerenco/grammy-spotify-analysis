import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
df = pd.read_csv("data/spotify_grammy_artist_data.csv")

# Basic data cleaning
df['Genres'] = df['Genres'].fillna('Unknown')
df['Followers'] = pd.to_numeric(df['Followers'], errors='coerce')
df['Grammy Wins'] = pd.to_numeric(df['Grammy Wins'], errors='coerce')

def dot_plot_by_grammy_wins(df):  
    # Dot Plot: Grammy Wins and Followers (Top 30 by Grammy Wins)
    top_grammy = df.sort_values(by='Grammy Wins', ascending=False).head(30)
    top_grammy = top_grammy.sort_values(by='Grammy Wins', ascending=True)
    top_grammy = top_grammy.dropna(subset=['Followers'])
    
    # Convert followers to millions
    top_grammy['Followers_M'] = top_grammy['Followers'] / 1_000_000

    # Create the plot
    plt.figure(figsize=(10, 6))

    plt.plot(top_grammy['Grammy Wins'], top_grammy['Artist'], 'bo', label='Grammy Wins', markersize=10)
    plt.plot(top_grammy['Followers_M'], top_grammy['Artist'], 'ro', label='Followers (in millions)', markersize=10)

    # Labels and Title
    plt.xlabel('Count')
    plt.title('Dot Plot: Grammy Wins and Followers (Top 30 Artists by Grammy Wins)')

    # Adding grid
    plt.grid(True, axis='x', linestyle='--', alpha=0.6)
    plt.grid(True, axis='y', linestyle='-', alpha=0.3)
    plt.legend(loc='lower right')

    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'Visualizations', 'grammy_dot_plot.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

def dot_plot_by_followers(df):  
    # Dot Plot: Followers and Grammy Wins (Top 30 by Grammy Wins)
    top_grammy = df.sort_values(by='Followers', ascending=False).head(30)
    top_grammy = top_grammy.sort_values(by='Followers', ascending=True)

    top_grammy = top_grammy.dropna(subset=['Followers'])

    # Convert followers to millions
    top_grammy['Followers_M'] = top_grammy['Followers'] / 1_000_000

    # Create the plot
    plt.figure(figsize=(10, 6))

    plt.plot(top_grammy['Grammy Wins'], top_grammy['Artist'], 'bo', label='Grammy Wins', markersize=10)
    plt.plot(top_grammy['Followers_M'], top_grammy['Artist'], 'ro', label='Followers (in millions)', markersize=10)

    # Labels and Title
    plt.xlabel('Count')
    plt.title('Dot Plot: Grammy Wins and Followers (Top 30 Artists by Followers)')

    # Adding grid
    plt.grid(True, axis='x', linestyle='--', alpha=0.6)
    plt.grid(True, axis='y', linestyle='-', alpha=0.3)
    plt.legend(loc='lower right')

    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'Visualizations', 'followers_dot_plot.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

dot_plot_by_followers(df)
dot_plot_by_grammy_wins(df)