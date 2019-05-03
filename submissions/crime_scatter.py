# -*- coding: utf-8 -*-
"""dat 4 toynbee crime final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HJY4SUA0fI_Xo0-TZHz-STyJiOUmLxLQ
"""

import matplotlib.pyplot as plt #to define plot parameters
import seaborn as sns #to graphical plots
import numpy as np #to math
import pandas as pd
import datetime as dt
import matplotlib.ticker as ticker

crime_df = pd.read_csv('https://raw.githubusercontent.com/research-at-toynbee-hall/datathons/master/datasets/datathon-2019-04-24/crime_in_london/cleaned/long_london_crime_2017-2019.csv')

crime_df['yearmonthday'] = crime_df['year_month'].apply(lambda x: dt.datetime.strptime(x, '%Y-%m-%d'))
crime_df['year'] = crime_df['yearmonthday'].dt.year

#changing the format to datetime so we can plot the chart
crime_df1 = crime_df.copy()
crime_df1.index = pd.to_datetime(crime_df1['yearmonthday'], format = '%Y-%m-%d')

sns.lmplot(x = 'year', y = 'count', data = crime_df1, fit_reg = False, hue = 'count', x_bins = 3, x_ci = None,  legend = False)
