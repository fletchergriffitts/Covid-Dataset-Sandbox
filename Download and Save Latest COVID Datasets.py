# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:04:38 2021
Download and save the latest .csv of COVID Datasets and save them locally
@author: Fletcher
"""



import pandas as pd



Newest_Hospital_Capacity = pd.read_csv("https://healthdata.gov/api/views/anag-cw7u/rows.csv?accessType=DOWNLOAD")      #Download and import the By-Facility Hospital Dataset online
Newest_Hospital_Capacity.to_csv("COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_Facility.csv")              #Save the file to update the dataset


