#!/usr/bin/env python
# coding: utf-8

# In[1]:


list = [1,2,3,4]


# In[3]:


list.count(3)


# In[1]:


#create a new object 
class Sample(object):
    pass


# In[2]:


x = Sample()


# In[5]:


type(x)


# In[17]:


class Dog(object):
    
    #class object attribute
    species = 'mammal'
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


# In[18]:


sam = Dog(breed = 'Lab', name = 'sam')


# In[19]:


sam


# In[9]:


sam.breed


# In[20]:


sam.name


# In[41]:


class Circle(object):
    
    #class object attribute 
    pi = 3.14
    
    def __init__ (self, radius =1):
        self.radius = radius
    
    def area(self):
        #radius**2 * pi = area
        return (self.radius**2) * Circle.pi 
    
    def set_radius(self, new_radius):
        
        """
        This method takes in a new radius and resets current radius.
        """
        self.radius = new_radius
    
    def get_radius(self):
        return self.radius
    
    def circumference(self):
        #diameter = 2 * radius 
        #circumference = diameter * pi
        return (self.radius * 2) * Circle.pi


# In[42]:


c = Circle(radius = 25)


# In[43]:


c.radius


# In[46]:


c.area()


# In[47]:


c.set_radius(35)


# In[48]:


c.radius


# In[49]:


c.area()


# In[50]:


c.get_radius()


# In[51]:


c.circumference()


# In[78]:


#Inheritance Example classes Animal and Dogs 
class Animal(object):
    
    def __init__ (self):
        print("Animal created")
    
    def whoAmI (self):
        print("Animal")
    
    def eat(self):
        print("Eating")


# In[93]:


class Dogs (Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        
    def WhoAmI(self):
        print("dog")
    
    def bark(self):
        print("Whoof")


# In[94]:


d = Dogs()


# In[95]:


d.WhoAmI()


# In[96]:


d.bark()


# In[98]:


d.eat()


# In[ ]:




