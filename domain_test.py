#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:10:37 2024

@author: Bodhi Global Analysis
@title: WFP Somalia WEAI Domain Test
@dataset reference: Women's empowerment in agriculture (WEAI) pilot II for Uganda
 - https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KUSXJR
 
This code is designed to verify that Python can accurately calculate the domains of the WEAI (Women's Empowerment in Agriculture Index). 
To do this, it measures Indicators 1.1 and 1.2.
"""
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

# Data Loading

file_path = 'data/012_ind_merged_uga_WEAI_1.1.dta'
file_path2 = 'data/test.xlsx'

data = pd.read_stata(file_path) # Open-source WEAI dataset (from IFPRI)
df = pd.read_excel(file_path2) # Dummy dataset for the domain test (from Bodhi)

df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
data = data.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Data Pre-processing

def preprocessing(df, new_col, drop_col, d_type = None):
    df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    
    if d_type == None:
        df.columns = new_col
        df.drop(columns=drop_col, inplace = True)
    
    elif d_type == 'open':
        df.drop(columns=drop_col, inplace = True)
        df.columns = new_col
        replace_dict = {'input into most or all decisions': "input into most decisions","no input or input in few decisions":"no input"}
        df = df.dropna(subset=['G1.03', 'G2.01.A', 'feelinputdecagr', 'raiprod_any'])
        df['G2.02.A'] = df['G2.02.A'].replace(replace_dict)
        df['G2.03.A'] = df['G2.03.A'].replace(replace_dict)
        df['G2.02.B'] = df['G2.02.B'].replace(replace_dict)
        df['G2.03.B'] = df['G2.03.B'].replace(replace_dict)
        df['G2.02.C'] = df['G2.02.C'].replace(replace_dict)
        df['G2.03.C'] = df['G2.03.C'].replace(replace_dict)
        df['G2.02.F'] = df['G2.02.F'].replace(replace_dict)
        df['G2.03.F'] = df['G2.03.F'].replace(replace_dict)
    
    df.reset_index(drop=True, inplace=True)
    return df

# New column names for the dummy dataset
new_col = ['start','end','G1.01','G1.02','G1.03','G1.04','G1.05','G1.06','G1.07',
 'G2.01.A','G2.02.A','G2.03.A','G2.01.B','G2.02.B','G2.03.B',
 'G2.01.C','G2.02.C','G2.03.C','G2.01.D','G2.02.D','G2.03.D','G2.01.E','G2.02.E','G2.03.E',
 'G2.01.F','G2.02.F','G2.03.F','G5.01.A','G5.02.A','G5.03.A','G5.04.A','G5.05.A','G5.01.B',
 'G5.02.B','G5.03.B','G5.04.B','G5.05.B','G5.01.C','G5.02.C','G5.03.C','G5.04.C','G5.05.C',
 'G5.01.D','G5.02.D','G5.03.D','G5.04.D','G5.05.D','_id','_uuid','_submission_time','_validation_status',
 '_notes','_status','_submitted_by','__version__','_tags','_index']

# List of columns that need to be dropped from the dummy dataset
drop_col = ['start','end','_id','_uuid','_submission_time','_validation_status',
 '_notes','_status','_submitted_by','__version__','_tags','_index']

# New column names for the open-source WEAI dataset
col_new = ['a01','a05','G1.03', 'hh_type','pilot', 'cluster', 'g1_06_p1',
 'G2.01.A','G2.02.A', 'G2.03.A', 'G2.01.B','G2.02.B', 'G2.03.B', 'G2.01.C', 'G2.02.C', 'G2.03.C', 'G2.01.F', 'G2.02.F', 'G2.03.F',
 'G5.01.A', 'g5a_01b_p1_a', 'g5a_01c_p1_a',
 'G5.02.A', 'G5.01.B', 'g5a_01b_p1_b', 'g5a_01c_p1_b', 'G5.02.B',
 'G5.01.C', 'g5a_01b_p1_c', 'g5a_01c_p1_c',
 'G5.02.C', 'G5.01.D', 'g5a_01b_p1_d', 'g5a_01c_p1_d', 'G5.02.D', 'g5a_01a_p1_e', 'g5a_01b_p1_e',
 'g5a_01c_p1_e', 'g5a_02_p1_e', 'g5a_01a_p1_f','g5a_01b_p1_f', 'g5a_01c_p1_f', 'g5a_02_p1_f', 'g5a_01a_p1_g', 'g5a_01b_p1_g', 'g5a_01c_p1_g',
 'g5a_02_p1_g', 'G5.03.A', 'G5.04.A', 'G5.05.A',
 'G5.03.B', 'G5.04.B', 'G5.05.B', 'G5.03.C', 'G5.04.C',
 'G5.05.C', 'G5.03.D', 'G5.04.D', 'G5.05.D', 'feelinputdecagr', 'raiprod_any']

# List of columns that need to be dropped from the open-source WEAI dataset
drop_cols = [ 'g2_01_p1_d', 'g2_02_p1_d', 'g2_03_p1_d', 'g2_01_p1_e', 'g2_02_p1_e', 'g2_03_p1_e', 'g3a_01a_p1_a', 'g3a_01b_p1_a',
 'g3a_02a_p1_a', 'g3a_02b_p1_a', 'g3a_02c_p1_a', 'g3a_03a_p1_a', 'g3a_03b_p1_a', 'g3a_03c_p1_a',
 'g3a_04a_p1_a', 'g3a_04b_p1_a', 'g3a_04c_p1_a', 'g3a_05a_p1_a', 'g3a_05b_p1_a', 'g3a_05c_p1_a', 'g3a_06a_p1_a', 'g3a_06b_p1_a',
 'g3a_06c_p1_a', 'g3a_01a_p1_j', 'g3a_01b_p1_j', 'g3a_02a_p1_j', 'g3a_02b_p1_j', 'g3a_02c_p1_j',
 'g3a_03a_p1_j', 'g3a_03b_p1_j', 'g3a_03c_p1_j', 'g3a_04a_p1_j', 'g3a_04b_p1_j', 'g3a_04c_p1_j', 'g3a_05a_p1_j', 'g3a_05b_p1_j', 'g3a_05c_p1_j',
 'g3a_06a_p1_j', 'g3a_06b_p1_j', 'g3a_06c_p1_j', 'g3a_01a_p1_k', 'g3a_01b_p1_k', 'g3a_02a_p1_k', 'g3a_02b_p1_k',
 'g3a_02c_p1_k', 'g3a_03a_p1_k', 'g3a_03b_p1_k', 'g3a_03c_p1_k', 'g3a_04a_p1_k', 'g3a_04b_p1_k', 'g3a_04c_p1_k', 'g3a_05a_p1_k', 'g3a_05b_p1_k', 'g3a_05c_p1_k',
 'g3a_06a_p1_k', 'g3a_06b_p1_k','g3a_06c_p1_k','g3a_01a_p1_l', 'g3a_01b_p1_l','g3a_02a_p1_l',
 'g3a_02b_p1_l','g3a_02c_p1_l','g3a_03a_p1_l','g3a_03b_p1_l','g3a_03c_p1_l','g3a_04a_p1_l','g3a_04b_p1_l','g3a_04c_p1_l','g3a_05a_p1_l',
 'g3a_05b_p1_l', 'g3a_05c_p1_l', 'g3a_06a_p1_l', 'g3a_06b_p1_l', 'g3a_06c_p1_l',
 'g3a_01a_p1_m', 'g3a_01b_p1_m', 'g3a_02a_p1_m', 'g3a_02b_p1_m', 'g3a_02c_p1_m', 'g3a_03a_p1_m', 'g3a_03b_p1_m', 'g3a_03c_p1_m', 'g3a_04a_p1_m',
 'g3a_04b_p1_m', 'g3a_04c_p1_m', 'g3a_05a_p1_m', 'g3a_05b_p1_m', 'g3a_05c_p1_m','g3a_06a_p1_m', 'g3a_06b_p1_m',
 'g3a_06c_p1_m', 'g3a_01a_p1_n', 'g3a_01b_p1_n', 'g3a_02a_p1_n', 'g3a_02b_p1_n', 'g3a_02c_p1_n', 'g3a_03a_p1_n', 'g3a_03b_p1_n',
 'g3a_03c_p1_n', 'g3a_04a_p1_n', 'g3a_04b_p1_n', 'g3a_04c_p1_n', 'g3a_05a_p1_n', 'g3a_05b_p1_n', 'g3a_05c_p1_n', 'g3a_06a_p1_n', 'g3a_06b_p1_n',
 'g3a_06c_p1_n', 'g3a_01a_p1_b', 'g3a_01b_p1_b', 'g3a_02a_p1_b', 'g3a_02b_p1_b', 'g3a_02c_p1_b', 'g3a_03a_p1_b', 'g3a_03b_p1_b',
 'g3a_03c_p1_b', 'g3a_04a_p1_b', 'g3a_04b_p1_b', 'g3a_04c_p1_b', 'g3a_05a_p1_b', 'g3a_05b_p1_b',
 'g3a_05c_p1_b', 'g3a_06a_p1_b', 'g3a_06b_p1_b', 'g3a_06c_p1_b', 'g3a_01a_p1_c', 'g3a_01b_p1_c', 'g3a_02a_p1_c', 'g3a_02b_p1_c', 'g3a_02c_p1_c',
 'g3a_03a_p1_c', 'g3a_03b_p1_c', 'g3a_03c_p1_c', 'g3a_04a_p1_c', 'g3a_04b_p1_c', 'g3a_04c_p1_c', 'g3a_05a_p1_c', 'g3a_05b_p1_c',
 'g3a_05c_p1_c', 'g3a_06a_p1_c', 'g3a_06b_p1_c', 'g3a_06c_p1_c', 'g3a_01a_p1_d', 'g3a_01b_p1_d', 'g3a_02a_p1_d', 'g3a_02b_p1_d',
 'g3a_02c_p1_d', 'g3a_03a_p1_d', 'g3a_03b_p1_d', 'g3a_03c_p1_d', 'g3a_04a_p1_d', 'g3a_04b_p1_d', 'g3a_04c_p1_d', 'g3a_05a_p1_d', 'g3a_05b_p1_d',
 'g3a_05c_p1_d', 'g3a_06a_p1_d', 'g3a_06b_p1_d', 'g3a_06c_p1_d', 'g3a_01a_p1_e',
 'g3a_01b_p1_e', 'g3a_02a_p1_e', 'g3a_02b_p1_e','g3a_02c_p1_e', 'g3a_03a_p1_e', 'g3a_03b_p1_e', 'g3a_03c_p1_e','g3a_04a_p1_e', 'g3a_04b_p1_e',
 'g3a_04c_p1_e', 'g3a_05a_p1_e', 'g3a_05b_p1_e', 'g3a_05c_p1_e', 'g3a_06a_p1_e', 'g3a_06b_p1_e', 'g3a_06c_p1_e', 'g3a_01a_p1_f',
 'g3a_01b_p1_f', 'g3a_02a_p1_f', 'g3a_02b_p1_f', 'g3a_02c_p1_f','g3a_03a_p1_f', 'g3a_03b_p1_f', 'g3a_03c_p1_f', 'g3a_04a_p1_f',
 'g3a_04b_p1_f', 'g3a_04c_p1_f', 'g3a_05a_p1_f', 'g3a_05b_p1_f', 'g3a_05c_p1_f', 'g3a_06a_p1_f', 'g3a_06b_p1_f', 'g3a_06c_p1_f', 'g3a_01a_p1_g',
 'g3a_01b_p1_g', 'g3a_02a_p1_g', 'g3a_02b_p1_g', 'g3a_02c_p1_g', 'g3a_03a_p1_g','g3a_03b_p1_g', 'g3a_03c_p1_g', 'g3a_04a_p1_g','g3a_04b_p1_g',
 'g3a_04c_p1_g','g3a_05a_p1_g', 'g3a_05b_p1_g', 'g3a_05c_p1_g', 'g3a_06a_p1_g', 'g3a_06b_p1_g', 'g3a_06c_p1_g', 'g3a_01a_p1_h',
 'g3a_01b_p1_h', 'g3a_02a_p1_h', 'g3a_02b_p1_h','g3a_02c_p1_h', 'g3a_03a_p1_h', 'g3a_03b_p1_h', 'g3a_03c_p1_h', 'g3a_04a_p1_h',
 'g3a_04b_p1_h', 'g3a_04c_p1_h', 'g3a_05a_p1_h', 'g3a_05b_p1_h', 'g3a_05c_p1_h', 'g3a_06a_p1_h', 'g3a_06b_p1_h','g3a_06c_p1_h',
 'g3a_01a_p1_i', 'g3a_01b_p1_i', 'g3a_02a_p1_i', 'g3a_02b_p1_i', 'g3a_02c_p1_i', 'g3a_03a_p1_i','g3a_03b_p1_i', 'g3a_03c_p1_i',
 'g3a_04a_p1_i', 'g3a_04b_p1_i', 'g3a_04c_p1_i', 'g3a_05a_p1_i', 'g3a_05b_p1_i', 'g3a_05c_p1_i', 'g3a_06a_p1_i',
 'g3a_06b_p1_i', 'g3a_06c_p1_i', 'g3b_07_p1_a', 'g3b_08a_p1_a', 'g3b_08b_p1_a', 'g3b_08c_p1_a', 'g3b_09a_p1_a', 'g3b_09b_p1_a',
 'g3b_09c_p1_a', 'g3b_07_p1_b', 'g3b_08a_p1_b', 'g3b_08b_p1_b', 'g3b_08c_p1_b', 'g3b_09a_p1_b', 'g3b_09b_p1_b',
 'g3b_09c_p1_b', 'g3b_07_p1_c', 'g3b_08a_p1_c', 'g3b_08b_p1_c', 'g3b_08c_p1_c', 'g3b_09a_p1_c', 'g3b_09b_p1_c', 'g3b_09c_p1_c',
 'g3b_07_p1_d', 'g3b_08a_p1_d', 'g3b_08b_p1_d', 'g3b_08c_p1_d', 'g3b_09a_p1_d', 'g3b_09b_p1_d', 'g3b_09c_p1_d', 'g3b_07_p1_e',
 'g3b_08a_p1_e', 'g3b_08b_p1_e', 'g3b_08c_p1_e', 'g3b_09a_p1_e', 'g3b_09b_p1_e', 'g3b_09c_p1_e', 'g4a_01_p1', 'g4a_02_p1', 'g4a_03_p1', 'g4b_03_p1_a', 'g4b_04_p1_a', 'g4b_03_p1_j',
 'g4b_04_p1_j', 'g4b_03_p1_b', 'g4b_04_p1_b', 'g4b_03_p1_c', 'g4b_04_p1_c', 'g4b_03_p1_d', 'g4b_04_p1_d', 'g4b_03_p1_e', 'g4b_04_p1_e',
 'g4b_03_p1_f', 'g4b_04_p1_f', 'g4b_03_p1_g', 'g4b_04_p1_g', 'g4b_03_p1_h', 'g4b_04_p1_h', 'g4b_03_p1_i', 'g4b_04_p1_i', 'g601_p1', 'g6_02_p1',
 'country', 'jown_count', 'jrightanyagr', 'credjanydec_any', 'incdec_count', 'groupmember_any', 'speakpublic_any', 'npoor_z105', 'leisuretime',
 '_5DE_id', '_5DE_score', '_5DE', 'GPI', 'GPI_id', 'GPI_gap', 'WEAI']

df = preprocessing(df, new_col, drop_col)
data = preprocessing(data, col_new, drop_cols, d_type = 'open')

# Function 1 to measure 'Indicator 1.1. Input in productive decisions'
def production_1(df, participate = ['G2.01.A', 'G2.01.B', 'G2.01.C', 'G2.01.F'], inputs = ['G2.02.A', 'G2.02.B', 'G2.02.C', 'G2.02.F']):
    
    df['production_decision1'] = 0

    for index, row in df.iterrows():
        count_1 = 0 
        for p_col, input in zip(participate, inputs):
            if row[p_col] == 'yes':
                if row[input] == 'no input':
                    count_1 += 0
                elif row[input] == 'input in few decisions':
                    count_1 += 0
                elif row[input] == 'no decision made':
                    count_1 += 0
                else: count_1 += 1
        df.at[index, 'production_decision1'] = count_1
    return df

# Function 2 to measure 'Indicator 1.1. Input in productive decisions'
def production_2(df, decision_makers = ['G5.01.A','G5.01.B','G5.01.C','G5.01.D'], extents = ['G5.02.A','G5.02.B','G5.02.C','G5.02.D']):
    
    df['production_decision2'] = 0

    for index, row in df.iterrows():
        count_1 = 0 
        for dm, extent in zip(decision_makers, extents):
            if row['G1.03'] == 'male' and row[dm] == 'main male or husband':
                count_1 += 1
            elif row['G1.03'] == 'female' and row[dm] == 'main female or wife':
                count_1 += 1
            elif row[dm] == 'self':
                count_1 += 1
            elif row[extent] == 'medium extent' or row[extent] == 'to a high extent':
                count_1 += 1

        df.at[index, 'production_decision2'] = count_1

    return df

# To calculate how many sub-indicators can be aggregated into the "indicator 1.1. Input in productive decisions”
def production_indicator(df):
    df['input_product_decision'] = 1
    df['cal_input'] = df['production_decision1'] + df['production_decision2']
    df['input_product_decision'] = df.apply(
        lambda row: 0 if row['cal_input'] > 1 else row['input_product_decision'],axis=1)
    df.drop(columns=['production_decision1', 'production_decision2','cal_input'], inplace = True)
    return df

# Function 2 to measure 'Indicator 1.2 Autonomy in production'
def autonomy(df, autonomy_cols_a = ['G5.03.A','G5.03.B','G5.03.C','G5.03.D'], 
             autonomy_cols_b = ['G5.04.A','G5.04.B','G5.04.C','G5.04.D'] , autonomy_cols_c = ['G5.05.A','G5.05.B','G5.05.C','G5.05.D']):
    score_map = {
        "never true": 1, 
        "not very true": 2, 
        "somewhat true": 3, 
        "always true": 4, 
        "decision not made": np.nan
    }

    for index, row in df.iterrows():
        for idx, (a_col, b_col, c_col) in enumerate(zip(autonomy_cols_a, autonomy_cols_b, autonomy_cols_c)):
            a = score_map.get(row[a_col], np.nan)
            b = score_map.get(row[b_col], np.nan)
            c = score_map.get(row[c_col], np.nan)
            
            if pd.isna(a) or pd.isna(b) or pd.isna(c):
                rai = np.nan
            else:
                rai = (-2 * a) - b + (3 * c)
                
            autonomy_col_name = f'autonomy_{idx + 1}'
            df.at[index, autonomy_col_name] = rai

    autonomy_cols = [f'autonomy_{i + 1}' for i in range(len(autonomy_cols_a))]
    df['autonomy'] = df[autonomy_cols].apply(lambda row: 0 if row.gt(1).any() else 1, axis=1)
    df.drop(columns=autonomy_cols, inplace = True)
    return df

# Generate the value of domain1 (indicators 1.1 and 1.2)
def domain_1(df):
    domain1_df = production_1(df)
    domain1_df = production_2(domain1_df)
    domain1_df = production_indicator(domain1_df)
    domain1_df = autonomy(domain1_df)
    return domain1_df

# Find the unmatched datapoints (original indicator value vs new indicator value from this Python code)
def unmatched_calculation(data):
    unmatched_rows = data[data['feelinputdecagr'] != data['input_product_decision']]
    row_count1 = len(unmatched_rows)
    index_list1 = unmatched_rows.index

    unmatched_rows2 = data[data['raiprod_any'] != data['autonomy']]
    row_count2 = len(unmatched_rows2)
    index_list2 = unmatched_rows2.index

    print(f"The number of unmatched datapoint [1.1. Input in productive decisions]: {row_count1}")
    print(f"The unmatched indices: {index_list1}")
    print("")
    print(f"The number of unmatched datapoint [1.2 Autonomy in production]: {row_count2}")
    print(f"The unmatched indices: {index_list2}")
    
df = domain_1(df)
df.to_csv('data/24-WFP-SO-1 domain_test.csv', index = False)
data = domain_1(data)
Ddata.to_csv('data/24-WFP-SO-1 open_source_result.csv', index = False)

unmatched_calculation(data)

"""
The 'unmatched_calculation' function identified four unmatched data points for Indicator 1.1, specifically at index numbers 152, 171, 178, and 215. 
However, after manually reviewing the data points, it was confirmed that the original indicator value was incorrectly calculated. 
Since the open-source dataset was used for pilot testing, it is believed that some miscalculations occurred.

For Indicator 1.2, all data points were matched.
"""