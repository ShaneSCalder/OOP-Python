#!/usr/bin/env python
# coding: utf-8

# In[1]:


l = [1,2,3]


# In[2]:


print(l)


# In[37]:


class Book(object):
    
    def __init__(self,title,author,pages):
        print("A book has been created")
        self.title =title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        
        return(
        "Title: %s, Author: %s, Pages: %s " %(self.title, self.author, self.pages)
        )
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("The book is gone") 


# In[38]:


b = Book("Python", "Mr. B", 100)


# In[39]:


b


# In[40]:


print(b)


# In[41]:


len(b)


# In[42]:


del b


# In[43]:


print(b)


# In[ ]:




