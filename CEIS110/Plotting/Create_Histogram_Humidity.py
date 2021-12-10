# -*- coding: utf-8 -*-
#Purpose: Create a histogram of humidity data from the first period
#Name: Steven Henderson
#Date: 11/29/21
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
df1['Humidity'].hist(bins=10, alpha=0.5); plt.suptitle('Histogram of Humidity 1')
plt.show()

