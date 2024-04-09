# -*- coding: utf-8 -*-
"""Seattle_NYC_Weather_Starter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FtbxiMlt3tcY6gbw4J61a2Y6kVZzsKRG

## Import libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style='whitegrid')
import missingno as msno

"""## Load the data

The NOAA National Centers for Environmental Information provides access to many types of environmental data, including records of daily precipitation.

We can use their [website](https://www.ncei.noaa.gov/cdo-web/search?datasetid=GHCND) to request records of daily precipitation from Seattle and New York (or other locations of interest) for the 3 year period January 2020 - January 2024.

The data are available at this [github repository](https://github.com/galenegan/DATA-3320/tree/main/weather) and are called `seattle_rain.csv` and `ny_rain.csv`.

Load the Seattle data set
"""

df_seattle = pd.read_csv('https://raw.githubusercontent.com/galenegan/DATA-3320/main/weather/seattle_rain.csv')

"""Load the New York data set"""

df_ny = pd.read_csv('https://raw.githubusercontent.com/galenegan/DATA-3320/main/weather/ny_rain.csv')

"""## Explore the Contents of the Datasets"""

df_seattle.describe()

df_ny.describe()

print(df_seattle.columns)
print(df_ny.columns)

"""Check data types"""

df_seattle.dtypes

df_ny.dtypes

"""## Do any data types need to be converted?"""

#convert DATE column to datetime format
df_seattle["DATE"] = pd.to_datetime(df_seattle["DATE"])
df_seattle.dtypes

df_ny["DATE"] = pd.to_datetime(df_ny["DATE"])
df_ny.dtypes

"""Exploratory Data Analysis

Graph precipitation for Seattle on each date
"""

fig, ax = plt.subplots()
ax.plot(df_seattle["DATE"], df_seattle["PRCP"])
ax.set_ylabel('Precipitation')
fig.autofmt_xdate()
fig.set_size_inches(15,5)

"""Graph precipitation for NYC on each date"""

fig, ax = plt.subplots()
ax.plot(df_ny["DATE"], df_ny["PRCP"])
ax.set_ylabel('Precipitation')
fig.autofmt_xdate()
fig.set_size_inches(15,5)

"""## Select relevant subsets of the data

Remove Unneccesary Variables
"""

df_seattle = df_seattle.drop(columns = ["ELEVATION","DAPR","MDPR","SNOW","SNWD","DASF","MDSF"])
df_ny = df_ny.drop(columns = ["ELEVATION","DAPR","MDPR","SNOW","SNWD","DASF","MDSF"])

"""Average by date

"""

df_seattle_avg = df_seattle.groupby(by="DATE", as_index = False)["PRCP"].mean()
df_ny_avg = df_seattle.groupby(by="DATE", as_index = False)["PRCP"].mean()

df_ny_avg.head(10)

df_seattle_avg.head(10)

"""Check number of observations are equal"""

print(len(df_ny_avg) == len(df_seattle_avg))

print(len(df_ny_avg)) #should be 1461 days, 365*4 + 1

"""## Random sample method"""

nkeep = 1461
df_seattle_subsample = df_seattle.sample(nkeep)
df_seattle_subsample = df_seattle_subsample.sort_values(by = "DATE")

"""Identify two stations from each state"""

df_seatac = df_seattle.loc[df_seattle["NAME"] =="SEATTLE TACOMA AIRPORT, WA US"]
df_jfk = df_ny.loc[df_ny["NAME"] =="JFK INTERNATIONAL AIRPORT, NY US"]

print(df_seatac.shape)
print(df_jfk.shape)

"""Merge data from both stations into one dataframe"""

df_port_merge = df_seatac[["DATE","PRCP"]].merge(df_jfk[["DATE","PRCP"]], on = "DATE", how = "right")

df_port_merge.head(5)

df_port_merge.head(20)

df_tidy = pd.melt(df_port_merge, id_vars = "DATE", var_name = "CITY", value_name = "Precipitation")

"""Ensure counts of both cities are equal"""

print(df_tidy['CITY'].value_counts())

"""Rename City variables accordingly"""

df_tidy.loc[df_tidy['CITY'] == 'PRCP_x','CITY'] = 'NYC'

df_tidy.loc[df_tidy['CITY'] == 'PRCP_y','CITY'] = 'Seattle'

df_tidy

df_tidy.head()

"""Check for Null Values"""

print(df_tidy[df_tidy['Precipitation'].isnull()])

"""Replace NAN values with average from that month across all 4 years"""

df_temp = df_tidy
df_temp['MONTH'] = df_tidy['DATE'].dt.month
#calculate the average precipitation for each month across all 4 years.
mean_prcp_bymonth = df_tidy.groupby(['CITY', 'MONTH'])['Precipitation'].mean()
mean_prcp_bymonth
#replace NaN values with the associated average value
df_tidy['Precipitation'] = df_tidy.apply(lambda row: mean_prcp_bymonth.loc[(row['CITY'], row['MONTH'])] if pd.isna(row['Precipitation']) else row['Precipitation'], axis=1)
df_temp['Precipitation'] = df_temp['Precipitation'].round(3)

"""Drop the temporary column"""

df_tidy.drop(columns=['MONTH'], inplace=True)
df_tidy

"""Test if NaN replacement worked"""

print(df_tidy[df_tidy['Precipitation'].isnull()])

df_tidy.describe()

"""#Export the dataframe as a CSV file"""

df_tidy.to_csv('clean_seattle_nyc_weather.csv', index=False)