#!/usr/bin/env python
# coding: utf-8

# ## 1D Arrays

# In[13]:


import numpy as np
arr1=[(1,2,3)]
arr1     #these are considered as list and not as arrays in numpy


# ## 2D Arrays

# In[4]:


import numpy as np 


# In[7]:


arr2=([1,2,3],[2,3,4])
arr2   # these are considered as list 


# # Array Creation
# 
# ## creating a X xY dimension array with zeros

# In[8]:


import numpy as np
np.zeros([2,3])


#  ## Creating a X x Y dimension array with interval z

# In[10]:


import numpy as np
np.arange(10,20,.5)


#  ### even numbers between 1 and 10

# In[12]:


import numpy as np
np.arange(2,10,2)


# ## Arrange  z numbers between X and Y

# In[17]:


import numpy as np 
np.linspace(0,10,5)


# ###### note in linspace each number or element in list has equal spacing (i.e)equidistant

# ## filling random numbers in an array of dimension X x Y

# In[19]:


import numpy as np
np.random.random((1,10))


# ## filling the array of dimension X x Y with a same element

# In[22]:


import numpy as np 
np.full((3,3),5)


# ## INSPECTING ARRAY  == CHECKINHG SIZE OF AN ARRAY

# In[27]:


import numpy as np
a=np.array([[1,2,3],[4,5,6,]])
print(np.shape(a))  # print (a.shape)


# In[31]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]]) # using array fn makes it as an array and without it its just a list
a.shape


# ## Resize the array

# In[34]:


import numpy as np
a=np.array([[1,2,3],[4,5,6,]])
a.shape=(3,2)
print(a)


# In[38]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]]) 
a.shape=(9,1)
print(a)


# In[40]:


import numpy as np  
a=np.array([[1,2,3],[4,5,6],[7,8,9]])  
a.shape=(9,2)# here it might go wrong because we are specifing more element than the elements actually present
print(a)


# ###### the trick in the above one in changing the shape is multipying the should give the no of elements
# (i.e) (9,1) will work because 9 x1 =9 but 9 X 2 = 18 so latter wont work because it exceeds the no of elements in array(a)

# ## return dimension of the array

# In[45]:


a= np.arange(24)
print(a.ndim)

#reshape
b=a.reshape(12,2) #trick=find factors of 24= 1,2,3,4,6,12,24
print(b.ndim)

c=a.reshape(2,3,4)
print(c.ndim)


# ### Number of elements in array

# In[49]:


a=np.arange(20)
print(a.size)

#example 2
b=np.arange(100)
print(b.size)


# In[64]:


arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.size) #Trick= rows=3 columns =3 so,3x3 =9



# In[65]:


#example2
arr2=np.array([[1,2,3],[4,5,6],[7,8,9,10]])
print(arr2.size)


# ## finding the datatype
# 

# In[67]:


a=np.arange(10)
a.dtype


# In[68]:


a=np.arange(2,10,dtype=float)
print(a)
print(a.dtype)


# # Array Mathematics
# 

# In[70]:


np.sum([10,20])


# In[72]:


a,b= 10,20
np.sum ([a,b]) #note : we are adding the a and b as an array (i.e) it is mentioned inside [ ] squarre bracets


# In[75]:


# adding two columns
np.sum([[10,20],[15,25]],axis=1)


# In[76]:


# adding two columns
np.sum([[10,20],[15,25]],axis=0)


# In[78]:


#what happes when no axis
np.sum([[10,20],[15,25]]) #it add all elements


# In[79]:


np.subtract(20,10)


# In[81]:


np.multiply(2,4)


# In[82]:


np.divide(10,5)


# In[86]:


a=10
print(np.exp(a))
print(np.sin(a))
print(np.cos(a))
print(np.sqrt(a))
print(np.log(a))


# ## ARRAY COMPARISON

# In[89]:


a=[1,2,3]
b=[1,2,3]
c=[4,5,6]
d=[1,2,5]
# it is a element wise comparison
print(np.equal(a,b))
print(np.equal(a,c))
print(np.equal(a,d))


# In[93]:


a=[1,2,3]
b=[1,2,3]
c=[4,5,6]

#it compares entire array

print(np.array_equal(a,b))
print(np.array_equal(a,c))


# ## aggregate function

# In[97]:


a=[1,2,3]

print("sum",np.sum(a))
print("min value",np.min(a))
print("mean",np.mean(a))
print("median",np.median(a))
print("standard deviation",np.std(a))
print("correlation coefficient",np.corrcoef(a))


# ## Broadcasting

# In[100]:


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3]])
print(a+b)


# # Array Manipulation

# In[102]:


a=np.array([1,2,3])
b=np.array([4,5,6])

#concatenating two arrays
print(np.concatenate((a,b)))


# In[104]:


#stack array row-wise:Vertically
np.vstack((a,b))


# In[105]:


#stack array hoerizontally
np.hstack((a,b))


# ## array splitting  

# In[109]:


new_arr=np.arange(16).reshape(4,4)
print(new_arr)


# In[118]:


#horizontal split
print(np.hsplit(new_arr,4)) # splitting into equal halves 
print("\n\n")
print(np.hsplit(new_arr,2))# spli into two equal parts


# In[130]:


print(np.hsplit(new_arr,np.array([3])))# split after the thrird column
print("\n\n")
print(np.hsplit(new_arr,np.array([1])))# split after the first column


# In[135]:


print(np.hsplit(new_arr,np.array([2,3])))# split second thrird column
print("\n\n")
print(np.hsplit(new_arr,np.array([0,2])))# split first and zeroth column


# In[136]:


##verical split
x = np.arange(16.0).reshape(4, 4)
x
np.vsplit(x, 2)


# ## Slicing

# In[138]:


a=np.array([[1,2,3],[4,5,6],[7,8,9]])
a[0]


# In[139]:


a[:1,1:]


# In[140]:


a[:3,2:]


# ## list vs numpy

# In[5]:


#numpy vs list:speed
import numpy as np
import sys

#define a list
l=range(1000)
print("size of list",sys.getsizeof(l)*len(l))

#define a numpy array 
a=np.arange(1000)
print("Size of array:",a.size*a.itemsize)


# In[19]:


#numpy vs list :speeed 
import time 
def using_list():
    t1=time.time()
    X=range(10000)
    Y=range(10000)
    Z=[X[i]+Y[i] for i in range(len(X))]
    return time.time()-t1

def using_Numpy():
    t1=time.time()
    a=np.arange(10000)
    b=np.arange(10000)
    
    z=a+b
    
    return time.time()-t1

list_time=using_list()
numpy_time=using_Numpy()
print(list_time,numpy_time)


# In[ ]:





# In[ ]:




