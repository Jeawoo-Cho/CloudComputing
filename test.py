#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
import requests
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote


# In[2]:



app = Flask(__name__)


# In[3]:


@app.route('/')
def index():
    return 'Hello Flask!'


# In[4]:


@app.route('/test')
def Call_api():
    xmlUrl = 'http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList'
    
    My_API_Key = unquote('laRplyI0NHo%2FgF2BdkTkFqSHArUwItA6rAMxOYqGIaAMk2o7W0N3jK7KhPfDKWj5%2FM4NCD%2FpfUOJM7tvMSs5Mg%3D%3D')
    
    para = '?' + urlencode(
        {
            quote_plus('ServiceKey') : My_API_Key,
            quote_plus('subwayStationId') : 'SUB228',
            quote_plus('dailyTypeCode') : '03',
            quote_plus('upDownTypeCode') : 'U'
        }
    )
    
    response = requests.get(xmlUrl + para).text.encode('utf-8')
    
    return response


# In[ ]:


if __name__ == '__main__':
    app.run(host='0.0.0.0')


# In[ ]:




