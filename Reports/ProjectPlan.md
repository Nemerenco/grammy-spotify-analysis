## Alexandra Nemerenco
### IS 477 Final Project Plan

### Overview

This project aims to explore the relationship between artists who are GRAMMY award winners and their listeners' trends on Spotify. I will be conducting a data analysis to identify patterns and visualize findings using Python libraries such as Pandas, Matplotlib, and Seaborn. The project will involve data collection, cleaning, analysis, and visualization to provide insights on the relationship between GRAMMY winners and their Spotify listeners. The goal is to understand how winning a GRAMMY award influences an artist's popularity on Spotify. The GRAMMY Awards highly prestigious and are often given by music industry professionals to recognize talent and excellence in the music industry. Winning a GRAMMY can significantly boost an artist's visibility and popularity, leading to increased listeners on platforms like Spotify. However, a high number of listeners does not always correlate with winning a GRAMMY. This analysis will look at this relationship from a closer perspective by combining data from both sources.

### Research Question

The primary research question for this project is: "How does winning a GRAMMY award influence an artist's popularity on Spotify, as measured by the number of followers?" In order to answer this question, I will combine the data from both sources and look at the patterns. Specifically, I will look at the following sub-questions:
1. What is the number of Spotify followers for GRAMMY-winning artists compared to non-GRAMMY-winning artists?
2. How does the number of Spotify listeners for artists who won a GRAMMY award in the past fare today?
3. Does genre play a significant role in the relationship between GRAMMY winners and their Spotify listeners?
4. Are there any patterns or trends in the songs or albums released by GRAMMY-winning artists?

### Team Members and Roles

Since this is an individual project, I will be the only person responsible for all aspects of the project. My roles will include:
- Writing the project plan
- Finding the data sources
- Accessing and collecting the data using scripts
- Cleaning, preprocessing, and integrating the data from both sources
- Analyzing and visualizing the data using Python libraries
- Creating an automated workflow that can execute the end-to-end analysis.
- Providing information and documentation on how to reproduce the analysis and results
- Compiling a document detailing software dependencies and a record of specific packages used
- Researching future work and potential improvements
- Documenting all the processes
- Providing references, citations, and license information for the data sources used
- Archiving the project files
- Writing the final report

### Datasets

The two primary datasets I will be using for this project are:
1. GRAMMY Winners Dataset: This dataset contains information about GRAMMY awards winners from 1958 yo 2019, including the year they won, the title of the award, the time the information was published and/or edited in the original source, the category of the award, the nominee song or album, the artist's name, other people who worked on the nominee, and image urls. The dataset can be found on Kaggle at the following link: https://www.kaggle.com/datasets/unanimad/grammy-awards/data. The data was originally extracted from the Awards' list page on the official GRAMMY website and IMDb. The dataset is in CSV format and uses the license CC0: Public Domain, which means it is free to use for any purpose without restrictions.
2. Spotify Monthly Listeners Dataset: This information will be directly accessed from the Spotify API. The dataset will include the number of monthly listeners for each artist, their genre, and other relevant information. The data will be collected using Python scripts that access the Spotify API and automated using Snakemake. The API documentation can be found at https://developer.spotify.com/documentation/web-api/. The data retrieved from the Spotify API is subject to its developer terms of service and usage policies outlined in the documentation. The data will be collected in JSON format, then converted to CSV for easier analysis. This way, I can ensure that the data is structured to match the GRAMMY dataset, making it easier to combine the two.

## Timeline 

Since this is an individual project, I will be following the timeline below alone:
- Week 1 (April 6 - April 12):
    - Familiarize myself with the GRAMMY dataset and Spotify API
    - Writing scripts to automatically access the GRAMMY Dataset from Kaggle and the Spotify API for data collection
    - Test the scripts to ensure they work correctly and can retrieve the necessary data
    - Document the process and steps that someone else would need to follow to reproduce the data collection
- Week 2 (April 13 - April 19):
    - Clean and preprocess the GRAMMY dataset
    - Familiarize myself with the Spotify API and its data structure
    - Combine the GRAMMY dataset with the data accessed from the Spotify API
    - Conduct exploratory data analysis to identify patterns and familiarize myself with the data
    - Document all the steps taken during the data cleaning and preprocessing stages
- Week 3 (April 20 - April 26):
    - Perform data analysis to answer the research questions
    - Create visualizations using Python libraries such as Matplotlib and Seaborn to illustrate the findings
    - Write Snakemake workflows to automate the data analysis and visualization process
    - Document the analysis process, including the steps required to repeat the workflow
- Week 4 (April 27 - May 3):
    - Create a reproducible package that includes all the scripts, analysis, and documentation
    - Document the software dependencies and packages
    - Document how the obtained data was used and any potential limitations and future work
    - Write the final report
    - Ensure that the project is well-organized and all files are properly named and structured
    - Archive the final project files
