#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


google_url = "https://www.google.com.tw/search"


keyword_input = input("輸入關鍵字:")

keyword = {'q':keyword_input}

r = requests.get(google_url,params = keyword)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text,'html.parser')
#     print(soup.prettify())
# print(soup)   
    items = soup.select('div.kCrYT > a[href^="/url"]')
    for i in items:
        print("標題:"+i.text)
        print("網址:"+i.get('href'))


# In[ ]:




