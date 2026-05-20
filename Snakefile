rule all:
    input:
        "logs/kaggle_check_done.txt",
        "logs/spotify_check_done.txt",
        "data/the_grammy_awards.csv",
        "data/spotify_grammy_artist_data.csv",
        "Visualizations/grammy_dot_plot.png",
        "Visualizations/followers_dot_plot.png"

rule check_kaggle:
    output:
        touch("logs/kaggle_check_done.txt")
    shell:
        """
        python scripts/check_kaggle_setup.py
        touch {output}
        """

rule check_spotify:
    output:
        touch("logs/spotify_check_done.txt")
    shell:
        """
        python scripts/check_spotify_setup.py
        touch {output}
        """

rule download_kaggle_data:
    input:
        "logs/kaggle_check_done.txt"
    output:
        "data/the_grammy_awards.csv"
    shell:
        """
        python scripts/kaggle_prepare_data.py
        """

rule prepare_spotify_data:
    input:
        "data/the_grammy_awards.csv",
        "logs/spotify_check_done.txt"
    output:
        "data/spotify_grammy_artist_data.csv"
    shell:
        """
        python scripts/spotify_prepare_data.py
        """

rule generate_visualizations:
    input:
        "data/spotify_grammy_artist_data.csv"
    output:
        "Visualizations/grammy_dot_plot.png",
        "Visualizations/followers_dot_plot.png"
    shell:
        """
        python scripts/analysis.py
        """
