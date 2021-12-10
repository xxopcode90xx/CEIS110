# -*- coding: utf-8 -*-
#Purpose: Create scatter plot of humidity for period 1 and period 2. Can replace df1 to df2 to display second period data
#Name: Steven Henderson
#Date: 11/29/21
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
plt.scatter(df2.index.values,df2['Humidity']); plt.suptitle('Humidity Period 2')
plt.show()
