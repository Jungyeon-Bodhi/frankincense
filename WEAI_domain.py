#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:34:53 2024

@author: Bodhi Global Analysis
"""
import pandas as pd
import numpy as np

class Domain():
    def __init__(self, df):
         self.df = df

    # Function to measure 'Indicator 1.1. Input in productive decisions'
    def production_1(self):
        df = self.df
        participate = ['G2.01.A', 'G2.01.B', 'G2.01.C', 'G2.01.F']
        inputs = ['G2.02.A', 'G2.02.B', 'G2.02.C', 'G2.02.F']
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
        self.df = df
        return True

    # Function to measure 'Indicator 1.1. Input in productive decisions'
    def production_2(self):
        df = self.df
        decision_makers = ['G5.01.A','G5.01.B','G5.01.C','G5.01.D']
        extents = ['G5.02.A','G5.02.B','G5.02.C','G5.02.D']
        df['production_decision2'] = 0
        for index, row in df.iterrows():
            count_1 = 0 
            for dm, extent in zip(decision_makers, extents):
                if row['G1.04'] == 'male' and row[dm] == 'main male or husband':
                    count_1 += 1
                elif row['G1.04'] == 'female' and row[dm] == 'main female or wife':
                    count_1 += 1
                elif row[extent] == 'medium extent' or row[extent] == 'to a high extent':
                    count_1 += 1
            df.at[index, 'production_decision2'] = count_1
        self.df = df
        return True

    # To calculate how many sub-indicators can be aggregated into the "indicator 1.1. Input in productive decisions”
    def production_indicator(self):
        df = self.df
        df['input_product_decision'] = 0
        df['cal_input'] = df['production_decision1'] + df['production_decision2']
        df['input_product_decision'] = df.apply(lambda row: 1 if row['cal_input'] > 1 else row['input_product_decision'],axis=1)
        df.drop(columns=['production_decision1', 'production_decision2','cal_input'], inplace = True)
        self.df = df
        return True
    
    # Function to measure 'Indicator 1.2 Autonomy in production'
    def autonomy(self):
        df = self.df
        autonomy_cols_a = ['G5.03.A','G5.03.B','G5.03.C','G5.03.D']
        autonomy_cols_b = ['G5.04.A','G5.04.B','G5.04.C','G5.04.D']
        autonomy_cols_c = ['G5.05.A','G5.05.B','G5.05.C','G5.05.D']
        score_map = {"never true": 1, "not very true": 2, "somewhat true": 3, "always true": 4, 
                     "decision not made": np.nan}
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
        df['autonomy'] = df[autonomy_cols].apply(lambda row: 1 if row.gt(1).any() else 0, axis=1)
        df.drop(columns=autonomy_cols, inplace = True)
        self.df = df
        return True

    # Function to measure 'Indicator 2.1 Ownership of assets'
    def resources_1(self):
        df = self.df
        resources = ['G3.01a.A','G3.01a.B','G3.01a.C','G3.01a.D','G3.01a.E','G3.01a.F','G3.01a.G','G3.01a.H','G3.01a.I','G3.01a.J'
                ,'G3.01a.K','G3.01a.L','G3.01a.M','G3.01a.N']
        resources_own = ['G3.02.A','G3.02.B','G3.02.C','G3.02.D','G3.02.E','G3.02.F','G3.02.G','G3.02.H','G3.02.I','G3.02.J'
                ,'G3.02.K','G3.02.L','G3.02.M','G3.02.N']
        valid_values = ['self', 'self and partner/spouse jointly', 
                    'self and other household member(s)', 
                    'self and other outside people', 
                    'self, partner/spouse and other outside people']
        df['resources_1'] = 0
        for index, row in df.iterrows():
            count_1 = 0 
            for resource, own in zip(resources, resources_own):
                if row[resource] == 'yes' and resource not in ['G3.01a.D', 'G3.01a.F', 'G3.01a.K']:
                    if row[own] in valid_values:
                        count_1 += 1
            df.at[index, 'resources_1'] = count_1
        df['ownership_of_assets'] = 0
        df['ownership_of_assets'] = df.apply(lambda row: 1 if row['resources_1'] >= 1 else row['ownership_of_assets'],axis=1)
        df.drop(columns='resources_1', inplace = True)
        self.df = df
        return True
    
    # Function to measure 'Indicator 2.2 Purchase, sale, or transfer of assets'
    def resources_2(self):
        df = self.df
        resources = ['G3.01a.A','G3.01a.B','G3.01a.C','G3.01a.D','G3.01a.E','G3.01a.F','G3.01a.G']
        decision_making1 = ['G3.03.A','G3.03.B','G3.03.C','G3.03.D','G3.03.E','G3.03.F','G3.03.G']
        decision_making2 = ['G3.04.A','G3.04.B','G3.04.C','G3.04.D','G3.04.E','G3.04.F','G3.04.G']
        decision_making3 = ['G3.05.A','G3.05.B','G3.05.C','G3.05.D','G3.05.E','G3.05.F','G3.05.G']
        decision_making4 = ['G3.06.A','G3.06.B','G3.06.C','G3.06.D','G3.06.E','G3.06.F','G3.06.G']
        valid_values = ['self', 'self and partner/spouse jointly', 
                    'self and other household member(s)', 
                    'self and other outside people', 
                    'self, partner/spouse and other outside people']
        df['resources_2'] = 0
        for index, row in df.iterrows():
            count_1 = 0 
            for resource, dc1, dc2, dc3, dc4 in zip(resources, decision_making1, decision_making2, decision_making3, decision_making4):
                if row[resource] == 'yes' and resource not in ['G3.01a.D', 'G3.01a.F']:
                    if any(dc in valid_values for dc in [dc1, dc2, dc3, dc4]):
                        count_1 += 1
            df.at[index, 'resources_2'] = count_1
        df['purchase_sale_transfer'] = 0
        df['purchase_sale_transfer'] = df.apply(lambda row: 1 if row['resources_2'] >= 1 else row['purchase_sale_transfer'],axis=1)
        df.drop(columns='resources_2', inplace = True)
        self.df = df
        return True
        
    # Function to measure 'Indicator 2.3 Access to and decisions on credit'
    def resources_3(self):
        df = self.df
        credits = ['G3.07.A','G3.07.B','G3.07.C','G3.07.D','G3.07.E']
        decision_making1 = ['G3.08.A','G3.08.B','G3.08.C','G3.08.D','G3.08.E']
        decision_making2 = ['G3.09.A','G3.09.B','G3.09.C','G3.09.D','G3.09.E']
        valid_values = ['self', 'self and partner/spouse jointly', 
                    'self and other household member(s)', 
                    'self and other outside people', 
                    'self, partner/spouse and other outside people']
        df['resources_3'] = 0
        for index, row in df.iterrows():
            count_1 = 0 
            for credit, dc1, dc2 in zip(credits, decision_making1, decision_making2):
                if row[credit] not in ['no', "don't know"]:
                    if any(dc in valid_values for dc in [dc1, dc2]):
                        count_1 += 1
            df.at[index, 'resources_3'] = count_1
        df['access_credit'] = 0
        df['access_credit'] = df.apply(lambda row: 1 if row['resources_3'] >= 1 else row['access_credit'],axis=1) 
        df.drop(columns='resources_3', inplace = True)
        self.df = df
        return True

    # Function to measure 'Indicator 3.1 Control over the use of income'
    def income_1(self):
        df = self.df
        participates = ['G2.01.A', 'G2.01.B', 'G2.01.C', 'G2.01.D', 'G2.01.E', 'G2.01.F']
        inputs = ['G2.03.A', 'G2.03.B', 'G2.03.C', 'G2.03.D', 'G2.03.E', 'G2.03.F']
        valid_values = ['input into some decisions', 'input into most decisions', 'input into all decisions']
        df['income_1'] = 0
        for index, row in df.iterrows():
            count_1 = 0 
            for participate, input in zip(participates, inputs):
                if row[participate] == 'yes':
                    if row[input] in valid_values:
                        count_1 += 1
            df.at[index, 'income_1'] = count_1
        self.df = df
        return True

    # Function to measure 'Indicator 3.1 Control over the use of income'
    def income_2(self):
        df = self.df
        desicions = ['G5.01.E', 'G5.01.F']
        extents = ['G5.02.E', 'G5.02.F']
        valid_values = ['medium extent', 'to a high extent']
        df['income_2'] = 0
        for index, row in df.iterrows():
            count_1 = 0 
            for desicion, extent in zip(desicions, extents):
                if row['G1.04'] == 'male' and row[desicion] == 'main male or husband':
                    count_1 += 1
                elif row['G1.04'] == 'female' and row[desicion] == 'main female or wife':
                    count_1 += 1
                else:
                    if row[desicion] != 'decision not made' and row[extent] in valid_values:
                        count_1 += 1
            df.at[index, 'income_2'] = count_1
        self.df = df
        return True

    # To calculate how many sub-indicators can be aggregated into the "Indicator 3.1 Control over the use of income”
    def income_indicator(self):
        df = self.df
        df['control_over_income'] = 0
        df['cal_income'] = df['income_1'] + df['income_2']
        df['control_over_income'] = df.apply(lambda row: 1 if row['cal_income'] >= 1 else row['control_over_income'],axis=1)
        df.drop(columns=['income_1', 'income_2','cal_income'], inplace = True)
        self.df = df
        return True

    # To calculate how many sub-indicators can be aggregated into the "Indicator 4.1 Group membership”
    def leadership_1(self):
        df = self.df
        groups = ['G4.05.A', 'G4.05.B', 'G4.05.C', 'G4.05.D', 'G4.05.E', 'G4.05.F', 'G4.05.G', 'G4.05.H', 'G4.05.I', 'G4.05.J', 'G4.05.K']
        df['leadership_1'] = 0
        for index, row in df.iterrows():
            count_1 = 0 
            for group in groups:
                if row[group] == 'yes':
                    count_1 += 1
            df.at[index, 'leadership_1'] = count_1
        df['group_membership'] = 0
        df['group_membership'] = df.apply(lambda row: 1 if row['leadership_1'] >= 1 else row['group_membership'],axis=1)
        df.drop(columns='leadership_1', inplace = True)
        self.df = df
        return True
        
    # To calculate how many sub-indicators can be aggregated into the "Indicator 4.2 Speaking in Public”    
    def leadership_2(self):
        df = self.df
        speakings = ['G4.01','G4.02','G4.03']
        valid_values = ['yes, but with a great deal of difficulty', 'yes, but with a little difficulty',
                       'yes, fairly comfortable', 'yes, very comfortable']
        df['leadership_2'] = 0
        for index, row in df.iterrows():
            count_1 = 0 
            for speaking in speakings:
                if row[speaking] in valid_values:
                    count_1 += 1
            df.at[index, 'leadership_2'] = count_1
        df['speaking_public'] = 0
        df['speaking_public'] = df.apply(lambda row: 1 if row['leadership_2'] >= 1 else row['speaking_public'],axis=1)
        df.drop(columns='leadership_2', inplace = True)
        self.df = df
        return True

    # To calculate how many sub-indicators can be aggregated into the "Indicator 5.1 Workload”   
    def time_1(self):
        df = self.df
        work_activities = ['G6.01.E','G6.01.F','G6.01.G', 'G6.01.H', 'G6.01.I', 'G6.01.J', 'G6.01.K', 'G6.01.L', 'G6.01.M']
        df['time_1'] = 0
        for index, row in df.iterrows():
            count_1 = 0
            for work in work_activities:
                if pd.notna(row[work]):
                    count_1 += row[work]
            df.at[index, 'time_1'] = count_1
        df['workload'] = 0
        df['workload'] = df.apply(lambda row: 1 if row['time_1'] < 10.5 else row['workload'],axis=1)
        df.drop(columns='time_1', inplace = True)
        self.df = df
        return True

    # To calculate how many sub-indicators can be aggregated into the "Indicator 5.2 Leisure”   
    def time_2(self):
        df = self.df
        df['leisure'] = 0
        for index, row in df.iterrows():
            if row['G6.02'] >= 5:
                df.at[index, 'leisure'] = 1
        self.df = df
        return True

    # Generate the five domains analysis
    def domain_analysis(self):
        self.production_1()
        self.production_2()
        self.production_indicator()
        self.autonomy()
        self.resources_1()
        self.resources_2()
        self.resources_3()
        self.income_1()
        self.income_2()
        self.income_indicator()
        self.leadership_1()
        self.leadership_2()
        self.time_1()
        self.time_2()
        return self.df
