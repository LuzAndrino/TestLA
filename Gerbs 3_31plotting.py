# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv(r"C:\TestLA\thresholds_ger12to15.csv") #All gerbs

#Breaking it up by gerb
ger12 = df[0:12] #Noise Exposed
ger15 = df[12:24] #Noise Exposed
ger13 = df[24:36] #Control
ger14 = df[36:47] #Control

'''
#Seaborn point plot: Estimate of central tendency
#Plot by gerb
sns.pointplot(data = ger12, x="abr_type", y= "response_lvl", hue="pre_post",dodge=True,color = "purple")
plt.savefig("Gerbil_12 NE.png")

sns.pointplot(data = ger15, x="abr_type", y= "response_lvl", hue="pre_post",dodge=True,color = "red")
plt.savefig("Gerbil_15 NE.png")

sns.pointplot(data = ger13, x="abr_type", y= "response_lvl", hue="pre_post",dodge=True,color = "blue")
plt.savefig("Gerbil_13 Ctrl.png")

sns.pointplot(data = ger14, x="abr_type", y= "response_lvl", hue="pre_post",dodge=True,color = "green")
plt.savefig("Gerbil_14 Ctrl.png")

'''



#plt.plot(df.abr_type,df.response_lvl) #nope


