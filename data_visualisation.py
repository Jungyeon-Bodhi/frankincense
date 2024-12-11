#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:22:04 2024

@author: Bodhi Global Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bodhi_blue = (0.0745, 0.220, 0.396)
bodhi_grey = (0.247, 0.29, 0.322)
bodhi_primary_1 = (0.239, 0.38, 0.553)
bodhi_secondary = (0.133, 0.098, 0.42)
bodhi_tertiary = (0.047, 0.396, 0.298)
bodhi_complement = (0.604, 0.396, 0.071)
color_palette = [bodhi_primary_1, bodhi_complement, bodhi_tertiary, bodhi_blue, bodhi_grey, bodhi_secondary]


def bar_state(df, col1, col2, replace_dict, title, fontsize, output_file, custom_order=None):
    # Replace values in col1 using replace_dict
    df[col1] = df[col1].replace(replace_dict)
    
    # Define custom order if needed, adding 'Overall'
    if custom_order is not None:
        df[col1] = pd.Categorical(df[col1], categories=custom_order, ordered=True)

    # Grouping data
    grouped_data = df.groupby(col1)[col2].value_counts().unstack().fillna(0)
    
    # Calculate percentages
    percent_data = grouped_data.divide(grouped_data.sum(axis=1), axis=0) * 100  
    
    # Plot the stacked bar chart
    ax = grouped_data.plot(kind='bar', stacked=False, width=0.65, figsize=(12, 8),
                           color=[bodhi_primary_1, bodhi_complement, bodhi_tertiary, bodhi_blue, bodhi_grey, bodhi_secondary])
    
    # Add titles and labels
    plt.title(title, fontsize=fontsize + 2)
    plt.xlabel(' ')
    plt.ylabel('Count')
    plt.legend(prop={'size': fontsize})
    plt.xticks(rotation=0, fontsize=fontsize)
    
    # Annotate the bars with counts and percentages
    for container in ax.containers:
        for i, bar in enumerate(container):
            height = bar.get_height()
            if height > 0:  # Avoid displaying annotations for zero heights
                item = container.get_label()
                percentage = percent_data[item].iloc[i]
                label = f'{height:.0f}\n({percentage:.1f}%)'
                ax.text(bar.get_x() + bar.get_width() / 2, height, label, ha='center', va='bottom', fontsize=fontsize - 3.5)
    
    # Adjust the y-axis
    y_max = ax.get_ylim()[1]
    ax.set_ylim(0, y_max * 1.1)
    
    # Save the plot
    plt.savefig(output_file, bbox_inches='tight', dpi=600)
    
def weai_visual(data, title, fontsize, output_file):
    df = pd.DataFrame(data)
    plt.figure(figsize=(24, 10))
    ax = df.set_index('State').plot(kind='bar', stacked=False, color=color_palette, width=0.8)

    for container in ax.containers:
        for bar in container:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2.0, bar.get_y() + height, 
                    f'{height:.3f}', ha='center', va='bottom', fontsize=fontsize-2.7, color='black')


    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df['State'], rotation=0, ha='center', fontsize=fontsize-1)
    ax.tick_params(axis='y', labelsize=7)
    ax.set_ylim(0, 1.1)
    plt.title(title, fontsize=fontsize+2)
    plt.xlabel(' ')
    plt.ylabel(' ', fontsize=fontsize -2)
    plt.legend(prop={'size': fontsize-3})
    plt.savefig(output_file, bbox_inches='tight', dpi=600)
    
def stack_contribution(categories, title, value1, value2, label1, label2, fontsize, output_file):

    x = np.arange(2)
    
    total_value1 = sum(value1)
    total_value2 = sum(value2)
    
    bar_width = 0.5

    fig, ax = plt.subplots(figsize=(14, 8))

    bar1 = ax.bar(x[0], total_value1, bar_width, label=label1, color=bodhi_primary_1, edgecolor='black')

    bar2 = ax.bar(x[1], total_value2, bar_width, label=label2, color=bodhi_complement, edgecolor='black')

    y_offset1 = 0
    y_offset2 = 0
    for i in range(len(categories)):
        ax.plot([x[0] - bar_width / 2, x[0] + bar_width / 2], [y_offset1 + value1[i], y_offset1 + value1[i]], color='black', lw=1)
        y_offset1 += value1[i]
        
        ax.plot([x[1] - bar_width / 2, x[1] + bar_width / 2], [y_offset2 + value2[i], y_offset2 + value2[i]], color='black', lw=1)
        y_offset2 += value2[i]

    for i in range(len(categories)):
        ax.text(x[0], sum(value1[:i+1]) - (value1[i] / 2), f'{categories[i]}: {value1[i]}', ha='center', va='center', fontsize=fontsize+4, color='white')
        ax.text(x[1], sum(value2[:i+1]) - (value2[i] / 2), f'{categories[i]}: {value2[i]}', ha='center', va='center', fontsize=fontsize+4, color='white')

    ax.set_xlabel('', fontsize=fontsize)
    ax.set_ylabel('', fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize + 6)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{label1}", f"{label2}"], fontsize=fontsize+4)
    ax.legend(fontsize=fontsize+3)
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight', dpi=600)


df = pd.read_excel('data/24-WFP-SO-1 - Data_cleaned.xlsx', index_col=0)

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
    "State": ["Oveall","Puntland", "Jubaland", "South West\nState", "Hirshabelle", "Galmudug", 'Somaliland'],
    "WEAI" : [0.695, 0.783, 0.600, 0.710, 0.671, 0.656, 0.720], # Please adjust these valuses manually
    "GPI" : [0.942, 0.960, 0.957, 0.951, 0.945, 0.920, 0.934],
    "5DE" : [0.667, 0.763, 0.560, 0.683, 0.641, 0.627, 0.696]}  # Please adjust these valuses manually

weai_visual(data, title = 'WEAI Scores | State', fontsize = 7, output_file = 'visuals/weai_scores.png')

data2 = {
    "State": ["Oveall","18 - 24", "25 - 34", "35 - 44", "45 - 54", "55 - 64", '65 and over'],
    "WEAI" : [0.695, 0.621, 0.661, 0.713, 0.724, 0.775, 0.603], # Please adjust these valuses manually
    "GPI" : [0.942, 0.925, 0.937, 0.948, 0.976, 0.942, 0.867],
    "5DE" : [0.667, 0.587, 0.630, 0.687, 0.696, 0.757, 0.573]}  # Please adjust these valuses manually

weai_visual(data2, title = 'WEAI Scores | Age Group', fontsize = 7, output_file = 'visuals/weai_scores_age.png')

# 4. Disempowerment Countribution rate visualisation
categories = ["Input in productive decisions",
    "Autonomy in production",
    "Ownership of assets",
    "Purchase, sale, or transfer of assets",
    "Access to and decisions on credit",
    "Control over the use of income",
    "Group membership",
    "Speaking in public",
    "Workload",
    "Leisure"]

female_values = [0.0624, 0.1296, 0.0547, 0.1276, 0.1748, 0.0342, 0.1503, 0.0849, 0.1071, 0.0746]

male_values = [0.0738, 0.1349, 0.0499, 0.1103, 0.1915, 0.0387, 0.1431, 0.0656, 0.1013, 0.0909]

title = 'Disempowerment Countribution Rate'

stack_contribution(categories, title, female_values, male_values, label1='Female', label2='Male', fontsize = 9, output_file = 'visuals/countribution_rate.png')