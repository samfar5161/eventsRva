# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:23:17 2024

@author: farle
"""

import requests
import datetime
import json
from bs4 import BeautifulSoup

def get_show_time(s):
    split_string = s.split('Show: ')
    time_value = split_string[1].strip()
    
    if (':' not in time_value):
        time_value = time_value[:-2] + ':00' + time_value[-2:]
        
    return time_value

funny_bone_sched_url = 'https://richmond.funnybone.com/calendar/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}     

content = requests.get(funny_bone_sched_url, headers=headers)
soup = BeautifulSoup(content.text, 'html.parser')


events = soup.find_all('div', class_='col-12 eventWrapper rhpSingleEvent py-4 px-0')


site_data = []
for e in events:
    event_title = e.find('h2', class_='font1by25 font1By5remMD marginBottom3PX lineHeight12 font1By75RemSM font1By5RemXS mt-md-0 mb-md-2').text.strip()
    event_date = e.find('div', id='eventDate').text.strip()
    event_time = e.find('span', class_='font0by75 fontWeight500 lineHeight15').text.strip()
    
    site_data.append([event_title, event_date, event_time])
    

output = []
possible_formats = ['%a, %b %d %Y','%a, %B %d %Y']
month_abrv = ['Mar','Apr','Aug','Sept','Oct','Nov']
month_full = ['May','June','July']
for r in site_data:
    event_title = r[0]
    event_time_string = get_show_time(r[2])
    event_time_obj = datetime.datetime.strptime(event_time_string, '%I:%M%p').time()
    
    for m in month_abrv:
        if m in r[1]:
            if 'Sept' in r[1]:
                r[1] = r[1].replace('Sept','Sep')
                
            event_date = datetime.datetime.strptime( r[1] + ' 2024', possible_formats[0])
            
        else:
            pass
        
    for m in month_full:
        if m in r[1]:
            event_date = datetime.datetime.strptime(r[1] + ' 2024', possible_formats[1])
        else:
            pass
      
    event_date = datetime.datetime.combine(event_date.date(), event_time_obj)    
    output.append([event_title, event_date.isoformat()])
    
    
with open('funnybone_events_output.json','w') as f:
    json.dump(output, f)
    
    
print('Process complete')
    
    
#%%


    