#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


data = pd.read_csv("/home/ali_hydir/Desktop/Semester 6/OPERATING SYSTEMS/CLASS/hello.txt", sep = "\t" , header = None)
print(data)
#data = data[1].str.split(" "  , expand = True)
#print(data)
#data = data[1].str.split("0m", expand =True)
#print(data)
#data[1].str.split("s" ,expand = True)


# In[ ]:





# In[2]:


dataa = pd.read_csv("/home/ali_hydir/Desktop/Semester 6/OPERATING SYSTEMS/CLASS/hello.txt", sep = "\t" , header = None )

dataa = dataa[1].str.split(" |0m|s"  , expand = True)
new_da = dataa[1].iloc[1::3]
float_n = new_da.apply(lambda x : float(x))
summ = float_n.sum()
print(summ)


# In[3]:


dataa = pd.read_csv("/home/ali_hydir/Desktop/Semester 6/OPERATING SYSTEMS/CLASS/hello2.txt", sep = "\t" , header = None )

dataa = dataa[1].str.split(" |0m|s"  , expand = True)
new_da = dataa[1].iloc[1::3]
float_n = new_da.apply(lambda x : float(x))
summ = float_n.sum()
print(summ)


# In[ ]:


dataa.info()


# In[ ]:





# In[ ]:




