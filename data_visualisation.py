#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:22:04 2024

@author: Bodhi Global Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt

bodhi_blue = (0.0745, 0.220, 0.396)
bodhi_grey = (0.247, 0.29, 0.322)
bodhi_primary_1 = (0.239, 0.38, 0.553)
bodhi_secondary = (0.133, 0.098, 0.42)
bodhi_tertiary = (0.047, 0.396, 0.298)
bodhi_complement = (0.604, 0.396, 0.071)
color_palette = [bodhi_primary_1, bodhi_complement, bodhi_tertiary, bodhi_blue, bodhi_grey, bodhi_secondary]


def bar_state(df, col1, col2, replace_dict, title, fontsize, output_file, custom_order = None):
    df[col1] = df[col1].replace(replace_dict)
    if custom_order != None:
        df[col1] = pd.Categorical(df[col1], categories=custom_order, ordered=True)
    grouped_data = df.groupby(col1)[col2].value_counts().unstack().fillna(0)
    # Calculate percentages
    percent_data = grouped_data.divide(grouped_data.sum(axis=0), axis=1) * 100  # Percent per province
    # Plotting the stacked bar chart
    ax = grouped_data.plot(kind='bar', stacked=False, figsize=(10, 6), color=[bodhi_primary_1, bodhi_complement, bodhi_tertiary, bodhi_blue, bodhi_grey, bodhi_secondary])
    plt.title(title, fontsize=fontsize+2)
    plt.xlabel(' ')
    plt.ylabel('Count')
    plt.legend(prop={'size': fontsize})
    plt.xticks(rotation=0, fontsize=fontsize)
    for container in ax.containers:
        for i, bar in enumerate(container):
            height = bar.get_height()
            item = container.get_label()
            percentage = percent_data[item].iloc[i]
            label = f'{height:.0f}\n({percentage:.1f}%)'
            ax.text(bar.get_x() + bar.get_width() / 2, 
                height, label, ha='center', va='bottom', fontsize=fontsize-2)
    y_max = ax.get_ylim()[1]
    ax.set_ylim(0, y_max * 1.1) 
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight', dpi=600)
    
def weai_visual(data, title, fontsize, output_file):
    df = pd.DataFrame(data)
    plt.figure(figsize=(24, 10))
    ax = df.set_index('Contents').plot(kind='bar', stacked=False, color=color_palette, width=0.8)

    for container in ax.containers:
        for bar in container:
            height = bar.get_height()  # 막대의 높이
            ax.text(bar.get_x() + bar.get_width() / 2.0, bar.get_y() + height, 
                    f'{height:.2f}', ha='center', va='bottom', fontsize=fontsize, color='black')


    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df['Contents'], rotation=0, ha='center', fontsize=fontsize-1)
    ax.tick_params(axis='y', labelsize=7)
    ax.set_ylim(0, 1.1)
    plt.title(title, fontsize=fontsize+2)
    plt.xlabel(' ')
    plt.ylabel('Index', fontsize=fontsize -2)
    plt.legend(prop={'size': fontsize})
    plt.savefig(output_file, bbox_inches='tight', dpi=600)

df = pd.read_excel('data/dummy_cleaned_2.xlsx', index_col=0)
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

df["G1.06"] = df["G1.06"].replace({"dual-adult household (male and female adult)":"dual-adult household"})

# 1. Respondents gender distribution 
replace_dict = {'puntland': 'Puntland', 'jubaland': 'Jubaland', 'south west state': 'South West State',
               "hirshabelle":"Hirshabelle", "galmudug":"Galmudug", "somaliland":"Somaliland"}

bar_state(df, 'G1.02a', 'G1.04', replace_dict, title = 'Respondents gender distribution | State',
         fontsize = 12, output_file = "visuals/gender_distribution.png")

# 2. Household type distribution (Single female households and dual-adult households)
bar_state(df, 'G1.02a', 'G1.06', replace_dict, title = 'Household type distribution | State',
         fontsize = 12, output_file = "visuals/household_distribution.png")


# 3. WEAI and GPI score visualisation
data = {
    "Contents": ["Puntland", "Jubaland", "South West\nState", "Hirshabelle", "Galmudug", 'Somaliland'],
    "WEAI" : [0.42, 0.48, 0.50, 0.37, 0.55, 0.20], # Please adjust these valuses manually
    "GPI" : [0.35, 0.55, 0.53, 0.43, 0.6, 0.22],}  # Please adjust these valuses manually

weai_visual(data, title = 'WEAI and GPI scores | State', fontsize = 9, output_file = 'visuals/weai_scores.png')