# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:52:47 2023

@author: ANDRINOL
"""
import pandas as pd
import matplotlib.pyplot as plt 



elevel = pd.read_csv(r"C:\TestLA\aging_noise_efr_lvl.csv")

#remove nans from lines 217-259
#nans in line 198-207 for ger 14-pre-1024. couldnt find the response level 




#Plot ger 12 efr level for pre and post 

#Create new dataframes for each gerb
ger12 = elevel[(elevel["subject"]=="ger12_22")] #Noise Exposed
ger13 = elevel[(elevel["subject"]=="ger13_22")] #Control
ger14 = elevel[(elevel["subject"]=="ger14_22")] #Control 
ger15 = elevel[(elevel["subject"]=="ger15_22")] #Noise Exposed


#Create new dataframes for each AM
ger12_40hz = ger12[(elevel["AM"]=="3kHz 40Hz AM")]




x = ger12_40hz[(ger12_40hz["pre_post"]=="pre")]
y =  ger12_40hz[(ger12_40hz["pre_post"]=="post")]

fig,ax = plt.subplots()
ax.plot(x.response_lvl,x.efr_lvl, color = "purple", marker="o")
ax.set_xlabel('Response')
ax.set_ylabel("EFR Level")
ax.set_title("Gerbil 12-22 3kHz Pre-test")


fig,ax = plt.subplots()

ax.plot(x.efr_lvl,x.response_lvl, color = "purple", marker="o") #pre
ax.set_xlabel('EFR Level')
ax.set_ylabel("Response")
#ax.set_title("Gerbil 12-22 3kHz Pre-test")

ax.plot(y.efr_lvl,y.response_lvl, color = "black", marker="^") #post
ax.set_xlabel('EFR Level')
ax.set_ylabel("Response")
ax.set_title("Gerbil 12-22 3kHz 40AM")

#include legend




