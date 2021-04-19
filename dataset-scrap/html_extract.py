# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:48:26 2021

@author: Victor
"""

import requests
from bs4 import BeautifulSoup
import os


# when week 21 --> year = 2021
def extractExcel(week):
    if week > 20:
        year = 2021
    else:
        year = 2020
    
    url = 'https://www.census.gov/data/tables/{}/demo/hhp/hhp{}.html'.format(str(year), str(week))
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, features='lxml')
    
    #print(soup.prettify())
    links = []
    for link in soup.find_all('a'):
        if link.get('href') is not None:
            if 'xlsx' in link.get('href'):
                links.append(link.get('href'))
            
    data_to_find = ['employ1', 'employ2', 'employ4', 'food1', 'housing1a', 'housing1b',
    'housing2a', 'housing2b', 'housing3a', 'housing3b', 'spending1', 'spending2', 'spending3']
    
    important_links = []
    
    
    for data in data_to_find:
        for url in links:
            if (data in url) & ('se' not in url) :
                important_links.append('http:'+url)
    
    
    
    directories = ['employ', 'food', 'housing', 'spending']
    
    for url in important_links:
        r = requests.get(url)
        
        if week > 9:
            cutoff = 66
        else:
            cutoff = 65
    
        if directories[0] in url:
            path = os.getcwd()+'/googleHacks/{}/'.format(directories[0])
        elif directories[1] in url:
            path = os.getcwd()+'/googleHacks/{}/'.format(directories[1])
        elif directories[2] in url:
            path = os.getcwd()+'/googleHacks/{}/'.format(directories[2])
        elif directories[3] in url:
            path = os.getcwd()+'/googleHacks/{}/'.format(directories[3])
        print(path+url[cutoff:])
    
        with open(path+url[cutoff:], 'wb') as f:
            f.write(r.content)
    
    
if __name__ == "__main__":
    for week in range(1, 28):
        extractExcel(week)
