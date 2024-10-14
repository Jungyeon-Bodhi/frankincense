#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:18:51 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import WEAI_data_preprocessing as dp

project_name = "WFP WEAI in Somalia"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/dummy"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/24-WFP-SO-1 Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

respondent_name = 'G1.03'
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = [respondent_name, '_id', '_uuid', 'G1.01', 'G1.04']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['start','end','G1.01','G1.02a','G1.02b-1','G1.02c-1-1','G1.02c-1-2','G1.02b-2','G1.02c-2-1',
 'G1.02c-2-2','G1.02b-3','G1.02c-3-1','G1.02c-3-2', 'G1.02b-4','G1.02c-4-1','G1.02c-4-2', 
 'G1.02b-5', 'G1.02c-5-1', 'G1.02c-5-2', 'G1.02b-6', 'G1.02c-6-1', 'G1.02c-6-2',
 'G1.03','G1.04','G1.05','G1.06','G1.07', 'G1.08a', 'G1.08b', 'G1.08c', 'G1.08d', 'G1.08e', 'G1.08f',
 'G2.01.A', 'G2.02.A', 'G2.03.A', 'G2.01.B', 'G2.02.B', 'G2.03.B', 'G2.01.C', 'G2.02.C', 'G2.03.C',
 'G2.01.D', 'G2.02.D', 'G2.03.D', 'G2.01.E', 'G2.02.E', 'G2.03.E', 'G2.01.F', 'G2.02.F', 'G2.03.F',
 'G3.01a.A', 'G3.01b.A', 'G3.02.A', 'G3.03.A', 'G3.04.A', 'G3.05.A', 'G3.06.A',
 'G3.01a.B', 'G3.01b.B', 'G3.02.B', 'G3.03.B', 'G3.04.B', 'G3.05.B', 'G3.06.B',
 'G3.01a.C', 'G3.01b.C', 'G3.02.C', 'G3.03.C', 'G3.04.C','G3.05.C', 'G3.06.C',
 'G3.01a.D', 'G3.01b.D', 'G3.02.D', 'G3.03.D', 'G3.04.D', 'G3.05.D', 'G3.06.D',
 'G3.01a.E', 'G3.01b.E', 'G3.02.E', 'G3.03.E', 'G3.04.E', 'G3.05.E', 'G3.06.E',
 'G3.01a.F', 'G3.01b.F', 'G3.02.F', 'G3.03.F','G3.04.F', 'G3.05.F', 'G3.06.F',
 'G3.01a.G', 'G3.01b.G', 'G3.02.G', 'G3.03.G', 'G3.04.G','G3.05.G', 'G3.06.G',
 'G3.01a.H', 'G3.01b.H', 'G3.02.H', 'G3.03.H', 'G3.04.H', 'G3.05.H', 'G3.06.H',
 'G3.01a.I', 'G3.01b.I', 'G3.02.I', 'G3.03.I', 'G3.04.I', 'G3.05.I', 'G3.06.I',
 'G3.01a.J', 'G3.01b.J', 'G3.02.J', 'G3.03.J','G3.04.J','G3.05.J', 'G3.06.J',
 'G3.01a.K', 'G3.01b.K', 'G3.02.K', 'G3.03.K', 'G3.04.K','G3.05.K', 'G3.06.K',
 'G3.01a.L', 'G3.01b.L', 'G3.02.L', 'G3.03.L', 'G3.04.L', 'G3.05.L', 'G3.06.L',
 'G3.01a.M', 'G3.01b.M', 'G3.02.M','G3.03.M', 'G3.04.M', 'G3.05.M', 'G3.06.M',
 'G3.01a.N', 'G3.01b.N', 'G3.02.N', 'G3.03.N', 'G3.04.N', 'G3.05.N', 'G3.06.N',
 'G3.07.A', 'G3.08.A', 'G3.09.A', 'G3.07.B', 'G3.08.B', 'G3.09.B', 'G3.07.C', 'G3.08.C', 'G3.09.C',
 'G3.07.D', 'G3.08.D', 'G3.09.D', 'G3.07.E', 'G3.08.E', 'G3.09.E', 'G4.01','G4.02','G4.03',
 'G4.04.A', 'G4.05.A', 'G4.04.B', 'G4.05.B', 'G4.04.C', 'G4.05.C', 'G4.04.D', 'G4.05.D',
 'G4.04.E', 'G4.05.E', 'G4.04.F', 'G4.05.F', 'G4.04.G', 'G4.05.G', 'G4.04.H', 'G4.05.H',
 'G4.04.I', 'G4.05.I', 'G4.04.J', "G4.05.J", 'G4.04.K', 'G4.04.K.o', 'G4.05.K',
 'G5.01.A', 'G5.01.B', 'G5.01.C', 'G5.01.D', 'G5.01.E', 'G5.01.F', 'G5.01.G',
 'G5.02.A', 'G5.03.A', 'G5.04.A', 'G5.05.A', 'G5.02.B', 'G5.03.B', 'G5.04.B', 'G5.05.B',
 'G5.02.C', 'G5.03.C', 'G5.04.C', 'G5.05.C', 'G5.02.D', 'G5.03.D', 'G5.04.D', 'G5.05.D','G5.02.E', 'G5.02.F', 'G5.02.G',
 "G6.01-i","G6.01-ii",'G6.01.A1','G6.01.A2','G6.01.B1','G6.01.B2','G6.01.C1','G6.01.C2','G6.01.D1','G6.01.D2','G6.01.E1',
 'G6.01.E2','G6.01.F1','G6.01.F2','G6.01.G1','G6.01.G2','G6.01.H1','G6.01.H2','G6.01.I1','G6.01.I2','G6.01.J1','G6.01.J2',
 'G6.01.K1','G6.01.K2','G6.01.L1','G6.01.L2','G6.01.M1','G6.01.M2','G6.01.N1','G6.01.N2','G6.01.O1','G6.01.O2','G6.01.P1',
 'G6.01.P2','G6.01.Q1','G6.01.Q2','G6.01.R1','G6.01.R1.0','G6.01.R2','G6.01.R2.0', 'G6.02',
 'OUTCOMEINTERVIEW', '_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by', '__version__', '_tags','_index']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['start','end','OUTCOMEINTERVIEW', '_id', '_uuid', '_submission_time', '_validation_status', '_notes', 
                 '_status', '_submitted_by', '__version__', '_tags','_index',  "G6.01-i", "G6.01-ii"]
# Specify the columns to be excluded from the data analysis

miss_col = ['G1.01','G1.02a','G1.04','G1.05','G1.06','G1.07','G1.08a', 'G1.08b', 'G1.08c', 'G1.08d', 'G1.08e', 'G1.08f',
           'G2.01.A','G2.01.B','G2.01.C','G2.01.D','G2.01.E','G2.01.F','G3.01a.A','G3.01a.B','G3.01a.C','G3.01a.D','G3.01a.E'
           ,'G3.01a.F','G3.01a.G','G3.01a.H','G3.01a.I','G3.01a.J','G3.01a.K','G3.01a.L','G3.01a.M','G3.01a.N','G3.07.A','G3.07.B'
           ,'G3.07.C','G3.07.D','G3.07.E','G4.01','G4.02','G4.03','G4.04.A','G4.04.B','G4.04.C','G4.04.D','G4.04.E','G4.04.F'
           ,'G4.04.G','G4.04.H','G4.04.I','G4.04.J','G4.04.K','G5.01.A', 'G5.01.B', 'G5.01.C', 'G5.01.D', 'G5.01.E', 'G5.01.F', 'G5.01.G',
           'G5.03.B','G5.03.C','G5.03.D', 'G6.01.A1','G6.01.B1', 'G6.01.C1', 'G6.01.D1', 'G6.01.E1', 'G6.01.F1', 'G6.01.G1',
           'G6.01.H1', 'G6.01.I1', 'G6.01.J1', 'G6.01.K1', 'G6.01.L1', 'G6.01.M1', 'G6.01.N1', 'G6.01.O1', 'G6.01.P1', 'G6.01.Q1','G6.02']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['G4.04.K.o','G6.01.R1.0','G6.01.R2.0']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = None
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['G1.08a', 'G1.08b', 'G1.08c', 'G1.08d', 'G1.08e', 'G1.08f']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])

regions = ['G1.02b-1','G1.02b-2','G1.02b-3','G1.02b-4', 'G1.02b-5', 'G1.02b-6']

locations = ['G1.02c-1-1','G1.02c-1-2','G1.02c-2-1','G1.02c-2-2','G1.02c-3-1','G1.02c-3-2','G1.02c-4-1','G1.02c-4-2', 
             'G1.02c-5-1', 'G1.02c-5-2', 'G1.02c-6-1', 'G1.02c-6-2']

"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

frankincense = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, identifiers, open_cols, cols_new, 
                                regions, locations, age_col, diss_cols, del_type = 0, file_type=file_type)
frankincense.processing()