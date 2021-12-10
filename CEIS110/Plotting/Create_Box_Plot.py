# -*- coding: utf-8 -*-
#Purpose: Create box plot for period data.
#Name: Steven Henderson
#Date: 11/29/21
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata2.csv")
df2.boxplot(); plt.suptitle('Period 2 box plot')
plt.show()


