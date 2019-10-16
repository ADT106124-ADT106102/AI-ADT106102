#!/usr/bin/env python
# coding: utf-8

# In[33]:


import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)

soup = BeautifulSoup(html.text,'html.parser')

# 取得開獎號碼的區塊(rightdown) 註* select取得的是陣列格式
lotteryArea = soup.select("#rightdown")
# print(data1)

# 進到威力彩區塊(contents_box02)
lottery = lotteryArea[0].find('div',{'class' : 'contents_box02'})
# print(data2)

# 取得所有開獎號碼(ball_green)
winNum = lottery.find_all('div',{'class':'ball_green'})             
# print(data3)

# 開獎號碼有六個，不過有分開出順序/大小順序，前者為前六個ball_green,後者為後六個
print("開出順序->",end = "")
for i in range(0,6):
    print(winNum[i].text,end="")
print("\n大小順序->",end = "")
for i in range(6,len(data3)):
    print(winNum[i].text,end="")
    
# 有一個第二區的開獎號碼(ball_red)要另外抓
red = lottery.find('div',{'class': 'ball_red'})
print("\n第二區->"+red.text)


# In[ ]:




