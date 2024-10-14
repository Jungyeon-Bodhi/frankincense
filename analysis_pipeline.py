#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:40:00 2024

@author: Bodhi Global Analysis
"""

import WEAI_domain as domain
import WEAI_analysis as bd
import pandas as pd

# Tag of the project
project_tag = "24-WFP-SO-1"

# Please assign the file path of the cleaned dataset
file_path = 'data/dummy_cleaned_2.xlsx' 

# Please assign the file path for data analysis matrix
file_path2 = "data/tables.xlsx"

# Please assign the file path for breakdown data
file_path3 = "data/tables_breakdown.xlsx"

# Please assign the file path for data analysis matrix
df = pd.read_excel(file_path)
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Run the domain analysis
domains = domain.Domain(df)
df = domains.domain_analysis()

# Run the weai analysis
weai = bd.WEAI(df, name='Overall', tag=project_tag)
weai.analysis(file_path2)

# Run the breakdown analysis
# breakdown_dic = {1:{var1:"Name of var1"}, 2:{var2:"Name of var2"}}
breakdown_dic = {1:{"Disability":"Disability"},2:{"G1.05":"Age Group"},3:{"G1.02a":"State"}}
weai.breakdown_save(breakdown_dic, file_path3)
