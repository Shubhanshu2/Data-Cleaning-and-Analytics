#!/usr/bin/env python
# coding: utf-8

# In[78]:


import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt
import seaborn as sns
import datetime


# In[79]:


WM = pd.read_csv('C:\\Users\\Shubhanshu Sharma\\Documents\\Python Scripts\\LaqnData_OxfordRd_d.csv')
WM.head()


# In[80]:


WM.isnull().sum()


# In[81]:


WM1 = WM.dropna()
WM1.isnull().sum()


# In[82]:


WM1.head()


# In[83]:


WM1 = WM1[(WM1['Value']>0)]


# In[84]:


WM1.shape


# In[85]:


WM1['ReadingDateTime'] = pd.to_datetime(WM1['ReadingDateTime'])


# In[86]:


WM1.replace({'ug m -3 as NO 2':'ug m -3 as NO'}, inplace=True)
WM1.head()


# In[87]:


WA = pd.read_csv('C:\\Users\\Shubhanshu Sharma\\Documents\\Python Scripts\\LaqnData_Putney_d.csv')
WA.head()


# In[88]:


WA.isnull().sum()


# In[89]:


WA1 = WA.dropna()
WA1.isnull().sum()


# In[90]:


WA1.head()


# In[91]:


WA1 = WA1[(WA1['Value']>0)]
WM1.shape


# In[92]:


WA1['ReadingDateTime'] = pd.to_datetime(WA1['ReadingDateTime'])


# In[93]:


WA1.replace({'ug m -3 as NO 2':'ug m -3 as NO'}, inplace=True)
WA1.head()


# In[94]:


WA_WM_merged = pd.merge(WA1,WM1, how='outer')
WA_WM_merged.head()


# In[95]:


WA_WM_merged.tail()


# In[96]:


WA_WM_merged['Time']=[d.time() for d in WA_WM_merged['ReadingDateTime']]
WA_WM_merged.head()


# In[97]:


WA_WM_merged['ReadingDateTime'] = pd.DatetimeIndex(WA_WM_merged['ReadingDateTime'])
WA_WM_merged = WA_WM_merged.set_index('ReadingDateTime')
WA_WM_merged.head()


# In[98]:


WA_WM_merged1 = WA_WM_merged.between_time('00:00','9:00')
WA_WM_merged1.head()


# In[99]:


WA_WM_merged2 = WA_WM_merged.between_time('17:00','23:45')
WA_WM_merged2.head()


# In[100]:


WA_WM_merged_time = pd.concat([WA_WM_merged1, WA_WM_merged2])
WA_WM_merged_time.head()


# In[101]:


WA_WM_merged_time = WA_WM_merged_time.reset_index()
WA_WM_merged_time.head()


# In[105]:


sns.factorplot(x='Species', y='Value', hue='Site', kind='bar', data=WA_WM_merged_time)
plt.title('Air Pollutant value in Putney(WA9) and Oxford(WM6)')
plt.ylabel('Pollutant Value')
plt.show()


# In[103]:


WA_WM_merged_time1 =  WA_WM_merged.between_time('9:00', '17:00')
WA_WM_merged_time1.head()


# In[104]:


sns.factorplot(x='Species', y='Value', hue='Site', kind='bar', data=WA_WM_merged_time1)
plt.show()


# The impact of air pollution in the cities Oxford and Putney is considered in this Lab practical. John Doherty is about to move to a new residence within London and needs a suitable area to reside based on the air quality. I have carried out the analysis based on his working hours and required asks in the question, and projected which is the best suitable area for him to move to.
# The csv files containing the data was cleaned (missing values and null values) for better analysis. Imported required libraries and plots for executing the codes and plotting graphs. Analysed the best time for John Doherty to communte to his work to home and vice versa. Considered the time before and after his office hours, because his standard working hours are given as 9-5. The final visualization gives a better comparision about the average value of the air species present in the atmosphere in both places.
# Even though i have analysed data, excluding office hours, I did an extra analysis of the data during office hours because under certain situations, he may not be able to go to work. From the final visualization, it is clear that WA9 has got lesser pollutant rate. To conclude, I can say that WA9 is less polluted and he can chose to live in Putney.
# 

# In[ ]:




