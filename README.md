# WFP Somalia

## THE PROVISION OF CONSULTANCY SERVICES FOR CONDUCTING A STUDY ON THE WOMEN's EMPOWERMENT IN AGRICULTURE INDEX (WEAI)

1. 'domain_test' folder

-> 'domain_test.py' code is designed to verify that Python can accurately calculate the domains of the WEAI (Women's Empowerment in Agriculture Index)

-> To do this, it measures Indicators 1.1 and 1.2

-> Please download two datasets ('012_ind_merged_uga_WEAI_1.1.dta', 'data/test.xlsx') and then place them in the data folder

-> Dataset reference: Women's Empowerment in Agriculture (WEAI) pilot II for Uganda
      (https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KUSXJR)

2. Data preprocessing

-> Before run, please place a raw data into the 'data' folder

-> Run the 'data_preprocessing.py' code. This code works based on the 'WEAI_data_preprocessing.py' code

-> Please adjust variables or parameters if necessary
   
3. Data analysis
   
-> Before run, please run the data preprocessing code

-> Run the 'analysis_pipeline.py' code. This code uses the 'WEAI_analysis.py' and 'WEAI_domain.py' files

* Please download the following libraries
  
-> Pandas: https://pandas.pydata.org/ (Version: 2.2.3)

-> Numpy: https://numpy.org/ (Version: 2.1.1)

-> Matplotlib: https://matplotlib.org/ (Version: 3.8.0)

-> Openpyxl: https://openpyxl.readthedocs.io/en/stable/ (Version: 3.1.2)

4. Data Visualisation
-> Data visualisation code will be updated
