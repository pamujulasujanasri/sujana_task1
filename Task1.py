#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd
import re


# In[85]:


df=pd.read_csv('KaggleV2-May-2016.csv')


# In[86]:


df


# In[87]:


print("Total rows: ", df.shape[0])
print("Total columns: ", df.shape[1])


# In[88]:


df1=df.dropna()


# In[89]:


df1


# In[91]:


#print("Total rows: ", df.shape[0])
#print("Total columns: ", df.shape[1])
df1['ScheduledDay'] = pd.to_datetime(df1['ScheduledDay'])
df1['AppointmentDay'] = pd.to_datetime(df1['AppointmentDay'])


# In[92]:


df1


# In[93]:


df1.head()


# In[94]:


print("Data types: ", df1.dtypes)


# In[95]:


print("Missing values: ", df.isnull().sum())


# In[96]:


df1.info()


# In[97]:


#checking and removing duplicates
df1.duplicated()


# In[98]:


#converting column headers to lower case
#df1.headers.lowercase()
#df1.columns=df1.columns.str.strip()
cols=df1.columns
cols


# In[99]:


cols=[x.lower() for x in cols]


# In[100]:


cols


# In[101]:


cols_str=str(cols)
cols_str


# In[102]:


#removing special characters from the list cols
#col_str=re.sub("[^A-Z]","",cols_str,0,re.IGNORECASE)


# In[103]:


cols_str


# In[104]:


import ast


# In[105]:


cols_list=ast.literal_eval(cols_str)
cleaned_cols=[col.replace('-','').replace('_','')for col in cols_list]
print(cleaned_cols)


# In[107]:


#cleaned_cols=df1.columns


# In[108]:


#df1


# In[109]:


df1.columns=cleaned_cols


# In[110]:


print(df1.columns)


# In[111]:


df1


# In[114]:


df1['scheduledday'] = pd.to_datetime(df1['scheduledday'], format='%d-%m-%Y%H:%M:%S')


# In[115]:


df1


# In[ ]:




