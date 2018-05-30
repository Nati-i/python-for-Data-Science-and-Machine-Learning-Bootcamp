
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


import numpy as np


# In[6]:


x = np.linspace(0,5,11)
y = x**2


# In[5]:


x


# In[6]:


y


# In[11]:


plt.plot(x,y,'r-')
plt.show()


# In[12]:


plt.xlabel('X Label')


# In[13]:


plt.title('Title')


# In[14]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[15]:


fig = plt.figure()


# In[16]:


axes = fig.add_axes([0.1,0.1,0.8,0.8])


# In[17]:


fig


# In[18]:


axes.plot(x,y)
axes.set_xlabel()


# In[19]:


fig


# In[12]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes2.plot(y,x)
axes2.set_title('Smaller Plot')
axes1.set_title('Larger Plot')


# In[15]:


fig,axes=plt.subplots(nrows=1,ncols=2)
#axes.plot(x,y)
plt.tight_layout()


# In[62]:


axes


# In[22]:


fig,axes=plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)


# In[19]:


fig


# In[23]:


len(axes)


# In[30]:


fig = plt.figure(figsize=(5,5))



# In[35]:


fig, axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))

axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()


# In[36]:


fig.savefig('mine.pdf')

