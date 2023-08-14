#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import calendar

import datetime as dt

import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from IPython.display import HTML


# In[14]:


df = pd.read_csv('data.csv')
#displaying the dataframe
df.head()


# In[15]:


df.shape


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[15]:


df=df.dropna()


# In[14]:


df.isnull().sum()


# In[16]:


df.columns


# In[17]:


df.columns =['Region','Date','Frequency','Estimated Unemployment Rate (%)','Estimated Employed','Estimated Labour Participation Rate (%)','Area']


# In[18]:


df.head(3)


# In[19]:


df.describe()


# In[21]:


round(df[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']].describe().T,2)



# In[22]:


#grouping by 'Region' and finding mean values for the numerical columns
areaStats = df.groupby(['Area'])[['Estimated Unemployment Rate (%)',
                                      'Estimated Employed',
                                      'Estimated Labour Participation Rate (%)']].mean().reset_index()

#rounding the values to 2 decimal points
round(areaStats,2)#grouping by 'Region' and finding mean values for the numerical columns


# In[23]:


regionStats = df.groupby(['Region'])[['Estimated Unemployment Rate (%)',
                                      'Estimated Employed',
                                      'Estimated Labour Participation Rate (%)']].mean().reset_index()

#rounding the values to 2 decimal points
round(regionStats,2)#grouping by 'Region' and finding mean values for the numerical columns


# In[25]:


fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df.corr(), center=0, cmap='Blues')
ax.set_title('unemployment analysis')


# In[31]:


fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(df.corr(), center=0, cmap='BuPu', annot=True)


# In[36]:


heatMap = df[['Estimated Unemployment Rate (%)', 'Estimated Employed', 
              'Estimated Labour Participation Rate (%)']]

#constructing on heatMap with correlation values
heatMap = heatMap.corr()

#plotting the figure
plt.figure(figsize=(23,8))
sns.heatmap(heatMap, annot=True,cmap='PiYG', fmt='.3f', linewidths=1)
plt.title('heatMap')
plt.show()


# In[16]:


df = pd.read_csv('data.csv')
#displaying the dataframe
df.head()


# In[25]:


u_emp=df[['Area',' Estimated Unemployment Rate (%)']].groupby('Area').sum().sort_values(by=' Estimated Unemployment Rate (%)', ascending =False)
u_emp


# In[29]:


import plotly.express as pl
get_ipython().system('pip install kaleido')


# In[32]:


import plotly.express as px
df = pd.read_csv('data.csv')

fig = px.scatter(df, x="Area", y=' Estimated Unemployment Rate (%)', color=' Estimated Labour Participation Rate (%)',
                 title="Scatterplot")


fig.show(renderer='colab')
fig.show(renderer='notebook')


# In[35]:


plt.figure(figsize=(12,10))
plt.title('Unemployment In India')
sns.histplot(x=' Estimated Unemployment Rate (%)', hue="Area", data=df)
plt.show()


# In[37]:


plt.figure(figsize=(12,10))
plt.title('Unemployment In India State Wise')
sns.histplot(x=' Estimated Unemployment Rate (%)', hue="Region", data=df)
plt.show()


# In[ ]:




