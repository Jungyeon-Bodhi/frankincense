# WFP Somalia

## Conducting a study on the Women's Empowerment in Agriculture Index (WEAI)

1. 'domain_test' and 'dummy_test' folder

-> 'domain_test.py' code is designed to verify that Python can accurately calculate the domains of the WEAI (Women's Empowerment in Agriculture Index)

-> To do this, it measures Indicators 1.1 and 1.2

-> Please download two datasets ('012_ind_merged_uga_WEAI_1.1.dta', 'data/test.xlsx') and then place them in the data folder

-> Dataset reference: Women's Empowerment in Agriculture (WEAI) pilot II for Uganda
      (https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KUSXJR)
      
-> Inside the 'dummy_test' folder, you will find two datasets. The 'dummy 1' and 'dummy 2' statistic tables describe the 5DE, GPI, and WEAI scores for each dummy test.

2. Data preprocessing

-> Before run, please place a raw data into the 'data' folder

-> Run the 'data_preprocessing.py' code. This code works based on the 'WEAI_data_preprocessing.py' code

-> Please adjust variables or parameters if necessary
   
3. Data analysis
   
-> Before running the code, please execute the data preprocessing and create a 'visuals' folder

-> Please change the clean data name to "24-WFP-SO-1 - Data_cleaned.xlsx"

-> Run the 'analysis_pipeline.py' code. This code uses the 'WEAI_analysis.py' and 'WEAI_domain.py' files

* Please download the following libraries
  
-> Pandas: https://pandas.pydata.org/ (Version: 2.2.3)

-> Numpy: https://numpy.org/ (Version: 2.1.1)

-> Matplotlib: https://matplotlib.org/ (Version: 3.8.0)

-> Openpyxl: https://openpyxl.readthedocs.io/en/stable/ (Version: 3.1.2)

4. Data Visualisation
-> This script ('data_visualisation.py') generates three plots
      1) Respondents gender distribution
      2) Household type distribution (Single female households and dual-adult households)
      3) WEAI and GPI scores
      4) Disempowerment Contribution rates
