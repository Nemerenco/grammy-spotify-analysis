## Alexandra Nemerenco
### IS 477 Final Project Status (Interim) Report

### Update on Project Progress

Since starting the project, I have made progress and completed several tasks outlined in the project plan. Because I am working alone, I had to focus on one task at a time and make sure I understand each part before moving on to the next. Because of this, I am slightly behind schedule, but I am confident that I will catch up in the coming weeks. Since starting the project, I was able to complete all of the tasks outlined in the first week of the project plan and am currently working on the tasks outlined in the second week. More specifically, I have completed the following tasks:
- Familiarized myself with the GRAMMY dataset by reading the documentation and understanding the structure of the data on the Kaggle page. 
- Wrote a script to automatically access the GRAMMY dataset from Kaggle and download it to my local machine. The script uses the Kaggle API to authenticate and download the dataset in CSV format.
- Tested the script to ensure it works correctly and can retrieve the necessary data. The script successfully downloads the dataset and saves it in a specified directory.
- Wrote a script to check that the user has the necessary setup to access the Kaggle API using their own credentials. If the setup is not correct, the script provides instructions on how to install the Kaggle API and set up the credentials locally. I instructed the user to create a Kaggle account, generate an API token, and place it in the correct directory. I am not providing my own Kaggle API token for security reasons and to follow Kaggle's terms of service.
- Read on the Spotify API documentation to familiarize myself with the data structure and how to access it. I learned about the data available through the API and how to authenticate requests. The API returns data in JSON format, which I will later convert to CSV for easier analysis when I combine it with the GRAMMY dataset.
- Wrote a script to access the Spotify API using my own credentials and tested a few requests to retrieve some data about an artist (The Weeknd) to ensure that the API is working correctly. The script successfully retrieves data about the artist, including their genres, followers, and Spotify URL for example.
- To access the Spotify API, I had to create a Spotify developer account and generate an API token which is available for a limited time and then has to be renewed. I am not providing my own Spotify API token for security reasons and to follow Spotify's terms of service. Instead, I wrote a script that checks if the user has the necessary setup to access the Spotify API using their own credentials. If the setup is not correct, the script provides instructions on how to create a Spotify developer account, generate an API token, and place it in the correct directory. I also provided an example .env file that the user can copy and fill in with their own credentials.
- Organized the project files and created directories for the scripts, data, reports, and documentation.

### Updated Timeline

- Week 3 (April 20 - April 26):
    - Clean and preprocess the GRAMMY dataset
    - Combine the GRAMMY dataset with the data accessed from the Spotify API
    - Conduct exploratory data analysis to identify patterns
    - Perform data analysis to answer the research questions
    - Create visualizations using Python libraries such as Matplotlib and Seaborn to illustrate the findings
- Week 4 (April 27 - May 3):
    - Write Snakemake workflows to automate the data analysis and visualization process
    - Create a reproducible package that includes all the scripts, analysis, and documentation
    - Document the software dependencies and packages
    - Document how the obtained data was used and any potential limitations and future work
    - Write the final report
    - Ensure that the project is well-organized and all files are properly named and structured
    - Archive the final project files

### Changes to the Project Plan

As I was working on the project, I realized that I needed to adjust the timeline slightly to accommodate the complexity of the tasks. I had to spend more time familiarizing myself with the Spotify API than I initially anticipated, which caused a delay in the project schedule. However, I believe that was one of the more complicated tasks, and I am now more confident in my ability to work with the API and retrieve the necessary data. Additionally, I wrote scripts to check the user's setup for both the Kaggle API and the Spotify API, which will help ensure that anyone who wants to reproduce the analysis can do so without issues. I also provided instructions on how to set up their own APIs and access the data in case the user does not have the necessary setup. Although this took extra time, it is a necessary step to ensure that the project is reproducible while also following the terms and conditions for both Kaggle and Spotify APIs. Sharing my own API tokens would be a security risk because others may use my accounts without my permission to access the data and may get my accounts banned for abuse of the services.