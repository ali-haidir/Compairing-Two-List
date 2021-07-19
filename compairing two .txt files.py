#!/usr/bin/env python
# coding: utf-8

# In[13]:


def file(d1):
    l1 = []
    summ = 0
    with open(d1, "r") as f:
        for line in f.read().split("\n")[::2]:
            y =line.split("0m")[-1]
            y = y[:-1]
            l1.append(y)
            
        for i in range(1 , len(l1) , 2):
            f = float(l1[i])
            summ = summ + f
        #print(summ)
        return summ


# In[14]:


file("/home/ali_hydir/Desktop/Semester 6/OPERATING SYSTEMS/CLASS/hello.txt")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


Percentage speedup: (I-S)*100/I


# In[ ]:



    


# In[22]:


def file(d1):
    l1 = []
    summ = 0
    with open(d1, "r") as f:
        for line in f.read().split("\n")[::2]:
            y =line.split("0m")[-1]
            y = y[:-1]
            l1.append(y)
        for i in range(1 , len(l1) , 2):
            f = float(l1[i])
            summ = summ + f
            average = summ/50
        #print(summ)
        return average


# In[23]:


x = file("/home/ali_hydir/Desktop/Semester 6/OPERATING SYSTEMS/CLASS/hello.txt")
print(x)
y = file("/home/ali_hydir/Desktop/Semester 6/OPERATING SYSTEMS/CLASS/hello2.txt")
print(y)


# In[ ]:





# In[ ]:


Percentage speedup: (I-S)*100/I


# In[26]:


def compare_files(a1 , a2):
    x = file(a1)
    y = file(a2)
    print("file1 = " ,x)
    print("file2 = ",y)
    if y<x:
        print("file2 takes less amount of time  ") # which in our case is system call instruction 
        percentage = (x-y)*100/x
        print("percentage = " , percentage)
        return y
    else:
        print("file1 takes less amount of time ")
        return x
    


# In[27]:


compare_files("/home/ali_hydir/Desktop/Semester 6/OPERATING SYSTEMS/CLASS/hello.txt" , "/home/ali_hydir/Desktop/Semester 6/OPERATING SYSTEMS/CLASS/hello2.txt")


# ## 
