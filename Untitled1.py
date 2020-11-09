#!/usr/bin/env python
# coding: utf-8

# In[6]:


def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
  
  

i = input("Enter the number: ")
print(countSetBits(int(i)))


# In[28]:


import collections
s = input("Enter your word: ")
print(collections.Counter(s).most_common(1)[0])


# In[12]:


text= input("Enter your text")
  
# printing original string 
print ("The original string is : " +  text) 
  
# using split() 
# to count words in string 
res = len(text.split()) 
  
# printing result 
print ("The number of words in string are : " +  str(res)) 


# In[59]:


def print_arguments(function):
    print("The argument is", function)
    y = function + 2
    return y
    

result = print_arguments(3)
print("This will return",result)


# In[60]:


def multiply_output(function):
    
    y = function*2
    return y
    

result = multiply_output(3)
print("This will return",result)


# In[63]:


def augment_function(function, decorators):
    
    print("The argument is", function)
    y = function + 2
    return y

    x = decorators*2
    return x
    

result = augment_function(3,6)
print("This will return",result)


# In[ ]:




