# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:58:00 2021
Covid mess around
@author: Fletcher

Dataset obtained from: https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u
"""



#Import all useful python libraries as a convenient abbreviation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#Import the datasets and clean them up
Hospital_Capacity = pd.read_csv("COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_Facility.csv").replace(-999999, 2)   #read the .csv dataset and replace the -999999 values with 2 since all cases with <4 are recorded as -999999 to protect patient confidentiality

TN_Hospitals = Hospital_Capacity.query('state == ["TN"]')               #Extract the TN data into a new TN variable

time_frame = TN_Hospitals["collection_week"].unique()[::-1]             #Extract the collection week data into its own "time_frame" variable for plotting
sevdayavg_totalstaffedadulticubeds = np.array([])                       #Initialize a seven day moving average of total staffed ICU beds into a variable
sevdayavg_totalstaffedadulticubedsoccupied = np.array([])               #Initialize a seven day moving average of total occupied and staffed ICU beds into a variable
sevdayavg_totalstaffedadulticubedsoccupiedwithcovid = np.array([])      #Initialize a seven day moving average of total occupied and staffed ICU beds with confirmed COVID into a variable
for each in time_frame:                                                 #For each week of reporting...
    total = TN_Hospitals.query('collection_week == ["'+ each +'"]')["total_staffed_adult_icu_beds_7_day_avg"].sum()                                     #...add up the total adult ICU beds for each hospital in Tennessee...
    total_occupied = TN_Hospitals.query('collection_week == ["'+ each +'"]')["staffed_adult_icu_bed_occupancy_7_day_avg"].sum()                         #...add up the total adult occupied ICU beds for each hospital in Tennessee...
    total_occupied_withcovid = TN_Hospitals.query('collection_week == ["'+ each +'"]')["staffed_icu_adult_patients_confirmed_covid_7_day_avg"].sum()    #...add up the total adult occupied ICU beds with confirmed COVID for each hospital in Tennessee...
    sevdayavg_totalstaffedadulticubeds = np.append(sevdayavg_totalstaffedadulticubeds, total)                                                           #...append this week's total to an array of total adult ICU beds...
    sevdayavg_totalstaffedadulticubedsoccupied = np.append(sevdayavg_totalstaffedadulticubedsoccupied, total_occupied)                                  #...append this week's total to an array of total occupied adult ICU beds...
    sevdayavg_totalstaffedadulticubedsoccupiedwithcovid = np.append(sevdayavg_totalstaffedadulticubedsoccupiedwithcovid, total_occupied_withcovid)      #...append this week's total to an array of total occupied adult ICU beds with COVID...



#plotting
sns.set_theme(font_scale = 2)       #set the seaborn plotting library theme and increase the font size multiplier by 2

g1 = sns.lineplot(x = time_frame, y = sevdayavg_totalstaffedadulticubeds, color = "b", linewidth = 5)       #Graph 1 is a line plot of total adult ICU beds vs. collection week of the data

g2 = sns.lineplot(x = time_frame, y = sevdayavg_totalstaffedadulticubedsoccupied, color = "y", linewidth = 5)       #Graph 2 is a line plot of total adult occupied ICU beds vs. collection week of the data

g3 = sns.lineplot(x = time_frame, y = sevdayavg_totalstaffedadulticubedsoccupiedwithcovid, color = "r", linewidth = 5)      #Graph 3 is a line plot of total adult occupied ICU beds with confirmed COVID vs. collection week of the data


