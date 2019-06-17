#!/usr/bin/env python
# coding: utf-8

# <h1>Risk Examples</h1>

# In[73]:


class Risk(object):
    
    def __init__(self,des,prob,impact):
        print("risk item has been added")
        #Description
        self.des = des
        #Probability
        self.prob = prob
        #Finacial Impact
        self.impact = impact
        
    def contingency(self):
        #probability * finacialImpact = contingency 
        return (self.prob / 100) * self.impact 
    
    def __str__(self):
        
        return("Description: %s, Probability: %s, Impact: $%s"%(self.des,self.prob,self.impact))
        


# In[74]:


b = Risk("rain delay", 100, 50000)


# In[75]:


print(b)


# In[76]:


b.contingency()


# In[77]:


c =Risk("Material Delay", 30, 5000)


# In[78]:


print(c)


# In[79]:


c.contingency()


# In[ ]:




