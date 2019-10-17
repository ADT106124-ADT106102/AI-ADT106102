#!/usr/bin/env python
# coding: utf-8

# In[4]:


# ! pip3 install beautifulsoup4


# In[3]:


import requests
from bs4 import BeautifulSoup

url = 'https://tw.yahoo.com/'
r= requests.get(url)

if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'html.parser')
        
        stories = soup.find_all('a',class_='story-title')
        for s in stories:
            print("標題:"+s.text)
            print("網址:"+s.get('href'))
    


# In[ ]:




