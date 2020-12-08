#!/usr/bin/env python
# coding: utf-8

# In[28]:


#모듈 임포트
from flask import Flask
import requests
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import bs4


#지하철명 스트링 입력후 지하철명 ID를 반환하는 함수
def subcode(subN):
    url = 'http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getKwrdFndSubwaySttnList'
    
    myKey = unquote('laRplyI0NHo%2FgF2BdkTkFqSHArUwItA6rAMxOYqGIaAMk2o7W0N3jK7KhPfDKWj5%2FM4NCD%2FpfUOJM7tvMSs5Mg%3D%3D')
    
    para = '?' + urlencode({ quote_plus('ServiceKey') : myKey, quote_plus('subwayStationName') : subN })
    
    response = requests.get(url + para).text.encode('utf-8')
    
    xml = bs4.BeautifulSoup(response, 'lxml-xml')
    rows = xml.findAll('item')
    get = rows[0].find_all()
    
    return get[1].text
    

#지하철ID, 평일휴일, 상행하행 입력후 시간표를 반환하는 함수
def subtime(subID, day, updown):
    url = 'http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList'
    
    myKey = unquote('laRplyI0NHo%2FgF2BdkTkFqSHArUwItA6rAMxOYqGIaAMk2o7W0N3jK7KhPfDKWj5%2FM4NCD%2FpfUOJM7tvMSs5Mg%3D%3D')
    
    para = '?' + urlencode(
        {
            quote_plus('ServiceKey') : myKey,
            quote_plus('subwayStationId') : subID,
            quote_plus('dailyTypeCode') : day,
            quote_plus('upDownTypeCode') : updown,
            quote_plus('numOfRows') : '100'
        }
    )
    
    response = requests.get(url + para).text.encode('utf-8')
    
    xml = bs4.BeautifulSoup(response, 'lxml-xml')
    
    mylist = []
    num = 0
    
    for time in xml.findAll('item'):
        s = time.depTime.string
        n = time.subwayStationNm.string
        
        mystr = n+" "+s[0]+s[1]+"시 "+s[2]+s[3]+"분  출발"
        mylist.append(mystr)
    
    return mylist

