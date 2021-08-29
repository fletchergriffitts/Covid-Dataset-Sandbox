# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:58:00 2021
Covid mess around
@author: Fletcher
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#Import the datasets and clean them up
#Age = pd.read_excel("Public-Dataset-Age_2021-8-5.xlsx")
#County_New = pd.read_excel("Public-Dataset-County-New_2021-8-5.xlsx")
#Daily_Age_Group_Outcomes = pd.read_excel("Public-Dataset-Daily-Age-Group-Outcomes_2021-8-5.xlsx")
#Daily_Case_Info = pd.read_excel("Public-Dataset-Daily-Case-Info_2021-8-5.xlsx")
#Daily_County_Age_Group = pd.read_excel("Public-Dataset-Daily-County-Age-Group_2021-8-5.xlsx")
#Daily_County_Cases_5_18_Years = pd.read_excel("Public-Dataset-Daily-County-Cases-5-18-Years_2021-8-5.xlsx")
#Daily_County_Cases_17_25_Years = pd.read_excel("Public-Dataset-Daily-County-Cases-17-25-Years_2021-8-5.xlsx")
#Daily_Data_Snapshot = pd.read_excel("Public-Dataset-Daily-Data-Snapshot_2021-8-5.xlsx")
#MMWR_Week_Case_Count = pd.read_excel("Public-Dataset-MMWR-Week-Case-Count_2021-8-5.xlsx")
#RaceEthSex = pd.read_excel("Public-Dataset-RaceEthSex_2021-8-5.xlsx")

#Davidson = Daily_County_Age_Group.query('COUNTY == ["Davidson"]')
#Sullivan = Daily_County_Age_Group.query('COUNTY == ["Sullivan"]')

Hospital_Capacity = pd.read_csv("COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_Facility.csv").replace(-999999, 2)

TN_Hospitals = Hospital_Capacity.query('state == ["WI"]')

time_frame = TN_Hospitals["collection_week"].unique()[::-1]
sevdayavg_totalstaffedadulticubeds = np.array([])
sevdayavg_totalstaffedadulticubedsoccupied = np.array([])
sevdayavg_totalstaffedadulticubedsoccupiedwithcovid = np.array([])
for each in time_frame:
    total = TN_Hospitals.query('collection_week == ["'+ each +'"]')["total_staffed_adult_icu_beds_7_day_avg"].sum()
    total_occupied = TN_Hospitals.query('collection_week == ["'+ each +'"]')["staffed_adult_icu_bed_occupancy_7_day_avg"].sum()
    total_occupied_withcovid = TN_Hospitals.query('collection_week == ["'+ each +'"]')["staffed_icu_adult_patients_confirmed_covid_7_day_avg"].sum()
    sevdayavg_totalstaffedadulticubeds = np.append(sevdayavg_totalstaffedadulticubeds, total)
    sevdayavg_totalstaffedadulticubedsoccupied = np.append(sevdayavg_totalstaffedadulticubedsoccupied, total_occupied)
    sevdayavg_totalstaffedadulticubedsoccupiedwithcovid = np.append(sevdayavg_totalstaffedadulticubedsoccupiedwithcovid, total_occupied_withcovid)



#plotting
sns.set_theme(font_scale = 2)

g1 = sns.lineplot(x = time_frame, y = sevdayavg_totalstaffedadulticubeds, color = "b", linewidth = 5)
#leg = plt.legend()
#for legobj in leg.legendHandles:
#    legobj.set_linewidth(5)
g2 = sns.lineplot(x = time_frame, y = sevdayavg_totalstaffedadulticubedsoccupied, color = "y", linewidth = 5)

g3 = sns.lineplot(x = time_frame, y = sevdayavg_totalstaffedadulticubedsoccupiedwithcovid, color = "r", linewidth = 5)


