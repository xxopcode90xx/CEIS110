# -*- coding: utf-8 -*-
#Purpose: Create temperature plot comparing period 1 and period 2
#Name: Steven Henderson
#Date: 11/29/21
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv") #baseline data is period 1 (older)
df2 = pd.read_csv("formatdata2.csv") #data for period 2 (more recent)
plt.figure(); df1.Fahrenheit.plot(label = 'Period 1'); df2.Fahrenheit.plot(label = 'Period 2'); plt.legend(loc='best'); plt.suptitle('Temperature in Fahrenheit Period 1 VS Period 2')
plt.show()


