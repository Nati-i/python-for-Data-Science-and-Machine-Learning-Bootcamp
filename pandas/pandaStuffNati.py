
# coding: utf-8

# In[1]:


import panda 


# In[2]:


import numpy


# In[3]:


import pandas


# In[2]:


import numpy as np


# In[1]:


import pandas as pd


# In[8]:


labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b':20, 'c':30}


# In[9]:


labels


# In[11]:


pd.Series(data = my_data)


# In[12]:


pd.Series(data = my_data, index=labels)


# In[13]:


pd.Series(my_data, labels)


# In[15]:


pd.Series(arr, labels)


# In[16]:


pd.Series(d)


# In[17]:


ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])


# In[18]:


ser1


# In[19]:


import numpy as np
import pandas as pd


# In[20]:


from numpy.random import randn


# In[21]:


np.random.seed(101)


# In[22]:


df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y','Z'])


# In[23]:


df


# In[24]:


randn(5,4)


# In[27]:


df['W']


# In[28]:


type(df)


# In[29]:


type(df['W'])


# In[30]:


df.W


# In[31]:


df[['W', 'Z']]


# In[32]:


df['W']


# In[34]:


df['new'] = df['W'] + df['Y']


# In[35]:


df


# In[41]:


df.drop('new', axis=1,inplace=True)


# In[47]:


df


# In[46]:


df.drop('A', axis=0)


# In[49]:


df.shape


# In[53]:


df.loc['A']


# In[54]:


df.iloc[2]


# In[55]:


df.iloc[0]


# In[59]:


df.loc['B':'E','Y':'Z']


# In[60]:


df.loc[['A','B'],['W', 'Y']]


# In[61]:


df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y','Z'])


# In[62]:


df


# In[63]:


df > 0


# In[64]:


booldf = df > 0


# In[65]:


booldf


# In[66]:


df[booldf]


# In[69]:


df['W']>0


# In[70]:


df[df['W']>0]


# In[71]:


df


# In[74]:


resultdf = df[df['W']<0]


# In[75]:


resultdf


# In[76]:


resultdf['X']


# In[78]:


df[df['W']>0]['X']


# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


np.random.seed(101)


# In[5]:


df = pd.DataFrame(np.random.randn(5,4), ['A', 'B','C','D','E'],['W', 'X','Y','Z'])


# In[6]:


from numpy.random import randn


# In[7]:


df


# In[8]:


df>0


# In[9]:


booldf = df>0


# In[10]:


booldf


# In[11]:


df[booldf]


# In[12]:


df[df>0]


# In[13]:


df


# In[14]:


df['W']>0


# In[15]:


df['W']


# In[16]:


df['W']>0


# In[19]:


df[df['W']>0]


# In[20]:


df


# In[23]:


df[df['W']>0]


# In[24]:


resultdf = df[df['W']>0]


# In[26]:


resultdf['X']


# In[28]:


df[df['W']>0]['X']


# In[30]:


df[df['W']>0][['Y','X']]


# In[31]:


boolSeries = df['W']>0
boolSeries


# In[32]:


result = df[boolSeries]


# In[33]:


result


# In[34]:


result[['Y', 'X']]


# In[35]:


myCols = ['Y', 'X']


# In[36]:


result[myCols]


# In[39]:


df[boolSeries][myCols]


# In[40]:


df


# In[47]:


df[df['W']>0]


# In[51]:


df[df['W']<0]


# In[43]:


df


# In[46]:


df[df['W']>0][['X', 'Y', 'Z']]


# In[55]:


df[(df['W']>0) & (df['Y']>0)]


# In[58]:


df[(df['W']>0) & (df['Y']>1)]


# In[59]:


df[(df['W']>0) | (df['Y']>1)]


# In[60]:


df


# In[63]:


a = df.reset_index()


# In[62]:


df


# In[64]:


a


# In[66]:


a.reset_index()


# In[67]:


newInd = 'CA NY WY OR CO'.split()


# In[68]:


newInd


# In[77]:


strn = '1 2 3 4 5 6'.split()
s = []
for i in strn:
    s.append(int(i))
s


# In[71]:


strn


# In[78]:


newInd = 'CA NY WY OR CO'.split()


# In[79]:


newInd


# In[80]:


df['States'] = newInd


# In[81]:


df


# In[88]:


a = df.set_index('States')


# In[85]:


df


# In[89]:


a


# In[99]:


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[100]:


hier_index


# In[101]:


df = pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[102]:


df


# In[104]:


df.loc['G1']


# In[109]:


df.loc['G1']


# In[113]:


df.index.names = ['Groups', 'Num']


# In[114]:


df


# In[117]:


df.loc['G2'].loc[2]['B']


# In[120]:


df.loc['G1'].loc[2]


# In[119]:


df.xs('G1')


# In[121]:


df.xs(1, level='Num')


# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[4]:


d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}


# In[5]:


d


# In[6]:


df = pd.DataFrame(d)


# In[7]:


df


# In[8]:


df.dropna()


# In[13]:


df.dropna(axis=1)


# In[14]:


df.dropna(thresh=2)


# In[15]:


df


# In[16]:


df.fillna(value='FILL VALUE')


# In[17]:


df['A'].fillna(value=df['A'].mean())


# In[21]:


data = {'Company':['GOOGLE','GOOGLE','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[22]:


df = pd.DataFrame(data)


# In[23]:


df


# In[26]:


byComp = df.groupby('Company')


# In[27]:


byComp


# In[28]:


byComp.mean()


# In[29]:


byComp.std()


# In[33]:


byComp.sum()


# In[34]:


df.groupby('Company').sum().loc['FB']


# In[36]:


df.groupby('Company').max() #person in alphabetical order


# In[37]:


df.groupby('Company').min()


# In[44]:


a = df.groupby('Company').describe()


# In[55]:


a


# In[85]:


df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()


# In[58]:


df


# In[59]:


df.head()


# In[60]:


df['col2'].unique()


# In[61]:


df['col2'].nunique()


# In[62]:


df['col2'].value_counts()


# In[63]:


df


# In[65]:


df[(df['col1']>2) & (df['col2']==444)]


# In[66]:


def times2(x):
    return x*2


# In[67]:


df['col1'].apply(times2)


# In[ ]:


df['col3'].apply(lambda x: x*2)


# In[74]:


df


# In[76]:


df.drop('col1', axis=1)


# In[77]:


df.columns


# In[78]:


df


# In[79]:


df.sort_values(by='col2')


# In[80]:


df.isnull()


# In[3]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)


# In[82]:


data


# In[83]:


df


# In[84]:


df.pivot_table(values='D', index=['A','B'], columns='C')


# In[86]:


df


# In[87]:


df['col2'].describe()


# In[88]:


df.index


# In[4]:


df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()


# In[5]:


df.sort_values(by='col2')


# In[7]:


df.sort_values(by='col2',inplace=True)


# In[8]:


df


# In[9]:


pwd


# In[10]:


pd.read_csv('example')


# In[11]:


df = pd.read_csv('example')


# In[12]:


df


# In[15]:


df.to_csv('My_output',index=False)


# In[16]:


pd.read_csv('My_output')


# In[18]:


pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# In[19]:


df.to_excel('Excel_sample2.xlsx',sheet_name='NewSheet')


# In[20]:


data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')


# In[21]:


data


# In[22]:


type(data)


# In[23]:


data[0]


# In[31]:


usefulData = data[0]


# In[26]:


from sqlalchemy import create_engine


# In[27]:


engine = create_engine('sqlite:///:memory:')


# In[33]:


usefulData.to_sql('myTable2',engine)


# In[34]:


sqldf = pd.read_sql('myTable2',con=engine)


# In[35]:


sqldf


# In[19]:


a = '02/25'


# In[7]:


for i in a:
    print(i.split())


# In[16]:


a[3:5]


# In[17]:


def exp(cc):
    if int(cc[3:5])>=25:
        return True
    else:
        return False


# In[20]:


exp(a)


# In[24]:


email = 'email@gmail.com'


# In[25]:


email.split('@')[1]

