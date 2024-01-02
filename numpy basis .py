#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import bioinfokit


# In[4]:


np.sqrt(16)


# # Array Creation

# In[5]:


np.array([1,2,3])


# In[6]:


##type
arr1=np.array([1,2,3,4])
type(arr1)


# In[7]:


###2 
np.zeros((2,2))


# In[8]:


###3
np.random.random((2,3))


# In[19]:


Arr=np.full((3,2),5) 
#return a new array of a given shape 
#and data type filled with fill_value .
Arr


# # Array Initialization

# In[9]:


np.full((3,3),10)  #1.shape 3 rows and columns   2.value =10


# In[10]:


np.arange(10,20,2)


# # # linspace is for creating eqidistan values 
# #### it also has starting value, ending value and no of data points .
# ##### these data point are equidistant
# 

# In[11]:


np.linspace(10,20,5)


# # ARRAY INSPECTION
# 

# In[13]:


Arr=np.full((3,2),5) 
#return a new array of a given shape 
#and data type filled with fill_value .
Arr


# In[14]:


Arr.shape # no of r and c


# In[16]:


Arr.ndim # no of dimensions


# In[17]:


Arr.dtype #return datatype


# In[18]:


Arr.size # no of elements


# # simple math

# #### Addition

# In[20]:


np.sum([[1,2],[2,3]],axis=0) #row wise addition


# In[22]:


np.sum([[1,2],[6,3]],axis=1) #column wise addition


# In[4]:


np.sum([10,20])


# In[5]:


a,b=10,20


# In[6]:


np.sum([a,b])


# ##Array Mathematics

# In[7]:


arr1=np.array([[1,2,3],
              [4,5,6,],
              [7,8,9]])


# In[8]:


np.sum(arr1)


# In[9]:


np.sum(arr1,axis=0)


# In[10]:


np.sum(arr1,axis=1)


# In[11]:


np.multiply(5,4)


# In[12]:


np.divide(10,5)


# In[13]:


np.exp(25)


# In[14]:


np.subtract(10,[20,5])


# In[16]:


help(np.subtract)


# In[ ]:




