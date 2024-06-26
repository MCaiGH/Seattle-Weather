# Seattle vs NYC Weather Project
DATA 3320 01 Seattle Weather project
Authors: Michael Cai
The purpose of this project is to analyze data of percipitation in Seattle WA and New York City NY from January 1, 2020 to January 1, 2024 to determine which city gets more rainfall. 

I will be using Python via Google Colab to analyze and create visualizations to express the result. 

The data comes from the National Centers for Environmental Information online search tool
Data Source: https://www.ncei.noaa.gov/cdo-web/search?datasetid=GHCND
Data Doccumentation: https://www.ncei.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf

Data Cleaning in Dataset_cleaning.ipynb:
To clean and prepare our data for analysis, I began by identifying any problems with variable typing and sample sizes. I changed the Date variable to be in datetime format so it can be read by Python. I then removed all variables that were not relevant to our analysis. In my data cleaning, I decided to choose one weather station from each state to have a comparable number of observations. There were several null observations for certain days in the NYC dataset which I filled in with the averages of all NYC precipitation data in the same month as the observation. After cleaning the data, I reshaped the dataframe to have three columns, Date, City, and Precipitation, the three key variables for our analysis.
The clean dataframe was exported as clean_weather_data.csv

Data Analysis in Weather_Analysis.ipynb:
To analyze the data, I used Python to create visualizations that demonstrated key information about precipitation in Seattle and NYC, this includes viewing average rainfall across months and years, viewing frequency of rainfall, and visualizing the trend of daily rainfall.

# License
The data and code in this repository are available for unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

