
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[2]:


import numpy as np


# #### Create an array of 10 zeros 

# In[4]:


np.zeros(10)


# #### Create an array of 10 ones

# In[5]:


np.ones(10)


# #### Create an array of 10 fives

# In[6]:


5*(np.ones(10))


# #### Create an array of the integers from 10 to 50

# In[8]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[9]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[10]:


np.arange(9).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[11]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[13]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[14]:


np.random.randn(25)


# #### Create the following matrix:

# In[18]:


np.arange(0.01,1.01, 0.01).reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[19]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[3]:


mat = np.arange(1,26).reshape(5,5)
mat = np.arange(1,26).reshape(5,5)
mat


# In[44]:


arr = mat[2:,1:]
arr


# In[40]:





# In[68]:


mat[:,:5]


# In[42]:


arr[1][3]


# In[48]:


mat[:3,1:2]


# In[42]:





# In[56]:


mat[4:6,][0]


# In[46]:





# In[58]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3:5]


# In[49]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[59]:


np.sum(mat)


# #### Get the standard deviation of the values in mat

# In[60]:


np.std(mat)


# #### Get the sum of all the columns in mat

# In[5]:


mat.sum(axis=0)


# # Great Job!
