
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:


salaries = pd.read_csv('C:\projectData\Python-for-Data-Analysis\Pandas\Pandas Exercises\Salaries.csv')


# In[10]:


salaries.info()


# ** Check the head of the DataFrame. **

# In[236]:


salaries


# ** Use the .info() method to find out how many entries there are.**

# In[11]:


salaries.info()


# **What is the average BasePay ?**

# In[25]:


df = salaries['BasePay']
df.mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[26]:


salaries['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[37]:


df = salaries.set_index('EmployeeName').loc['JOSEPH DRISCOLL']
df.loc['JobTitle']
df


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[38]:


df.loc['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[59]:


highestPay = salaries.sort_values(by='TotalPayBenefits', ascending=False)
highestPay.head(1)


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[60]:


lowestPay = salaries.sort_values(by='TotalPayBenefits')
lowestPay.head(1)


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[73]:


averageBasePay = salaries.groupby(by='Year')
averageBasePay['BasePay'].mean()


# ** How many unique job titles are there? **

# In[75]:


uniqueTitles = salaries['JobTitle'].nunique()
uniqueTitles


# ** What are the top 5 most common jobs? **

# In[129]:


#commonJobs = salaries.groupby(by='JobTitle')
#commonJobs.size().sort_values(ascending=False).head()
salaries['JobTitle'].value_counts().head()


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[195]:


sal2013 = salaries[['Year', 'JobTitle']] 
sal2013 = sal2013[sal2013['Year']==2013]
sal2013 = sal2013['JobTitle'].value_counts()
sal2013 = sal2013[sal2013 == 1]
sal2013.sum()


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[5]:


containChef = salaries['JobTitle'].str.contains('Chief',regex=True,case=False)
containChef[containChef == True].sum()


# In[21]:





# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[23]:





# # Great Job!
