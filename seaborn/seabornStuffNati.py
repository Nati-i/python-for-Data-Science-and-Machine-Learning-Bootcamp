
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


tips = sns.load_dataset('tips')


# In[4]:


tips.head()


# In[12]:


sns.distplot(tips['total_bill'],kde=False,bins=40)


# In[19]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')


# In[22]:


sns.pairplot(tips,hue='sex',palette='cool')


# In[23]:


sns.rugplot(tips['total_bill'])


# In[24]:


sns.distplot(tips['total_bill'])


# In[25]:


tips


# In[26]:


tips.head()


# In[30]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# In[29]:


import numpy as np


# In[31]:


sns.countplot(x='sex',data=tips)


# In[33]:


sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')


# In[36]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)


# In[41]:


sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex',dodge=True)


# In[42]:


sns.swarmplot(x='day',y='total_bill',data=tips)


# In[43]:


sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')


# In[44]:


flights = sns.load_dataset('flights')


# In[45]:


flights.head()


# In[46]:


tc = tips.corr()
sns.heatmap(tc)


# In[47]:


tc


# In[48]:


sns.heatmap(tc,annot=True,cmap='coolwarm')


# In[54]:


fp = flights.pivot_table(index='month',columns='year',values='passengers')


# In[53]:


flights.head()


# In[67]:


sns.heatmap(fp,cmap='coolwarm',linecolor='white',linewidth=1)


# In[70]:


sns.clustermap(fp,cmap='coolwarm',standard_scale=1)


# In[71]:


iris = sns.load_dataset('iris')


# In[72]:


iris.head()


# In[73]:


iris['species'].unique()


# In[89]:


g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# In[80]:


import matplotlib.pyplot as plt


# In[88]:


t = sns.FacetGrid(data=tips,col='time',row='smoker')
t.map(plt.scatter,'total_bill','tip')


# In[5]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')


# In[6]:


tips.head()


# In[9]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],scatter_kws={'s':100})


# In[15]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',aspect=0.6,
           size=8
          )


# In[27]:


sns.set_style('ticks')
sns.countplot(x='sex',data=tips)
sns.set_context('notebook')
sns.despine()

