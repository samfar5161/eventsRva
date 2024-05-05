# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:02:20 2024

@author: farle

These functions are for retreiving the JSON file from The National RVA for 
parsing their event data so that we can populate an event calendar.
"""

# better functions for getting data from The National
# RVA's website


import requests
from bs4 import BeautifulSoup
import os
import json

def get_nationalrva_schedule_file():
    the_national_url = 'https://www.thenationalva.com/schedule/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}     
    response = requests.get(the_national_url, headers=headers)
    text = response.text
    
    soup = BeautifulSoup(text, 'html.parser')
    
    json_files = soup.find_all('div', attrs={'data-file': True})
    
    if len(json_files) == 1:
        schedule_file = str(json_files[0]['data-file'])
        
    elif len(json_files) > 1:
        print("ERROR - multiple potential schedule files found. Fix this code.")
        return 0
        
    return schedule_file


def check_file_exists(file_name):
    directory_path = '/'
    file_path = os.path.join(directory_path, file_name)
    return os.path.exists(file_path)


def compare_content(data_one, data_two):
    if (hash(data_one) == hash(data_two)):
        return True
    else:
        return False
  
      
def download_json_file():
    url = get_nationalrva_schedule_file()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
    response = requests.get(url, headers=headers)
    with open('theNational_newSched.json', 'w') as f:
        f.writelines(response.text)


def compare_files(file_one, file_two):
    with open(file_one, 'r') as f1:
        file_one_data = f1.read()
        
    with open(file_two, 'r') as f2:
        file_two_data = f2.read()
        
    return compare_content(file_one_data, file_two_data)


# don't use this. actually, use this. go for it.
def get_schedule_data(json_file):
    content = json.loads(json_file)
    events = content['events']
    data = []
    for event in events:
        acts = event['associations']['headliners']
        
        for act in acts:
            artist = act['name']    
                    
        if (event['eventDateTime']) == 'TBD' or event['doorDateTime'] == 'TBD':
            pass
        
        else:
            event_start_iso = event['eventDateTime']
        
        #data.append([artist, event_date, str(event_time), str(door_time), event_start_iso])
        data.append({'title':artist, 'start': event_start_iso})
    
    return data

## begin
print('Getting schedule data for The National RVA...')

download_json_file()
with open('theNational_newSched.json','r') as f:
    content = f.read()
    
data = get_schedule_data(content)

with open('TheNational_events_output.json', 'w') as f:
    file = json.dumps(data)
    f.write(file)

print('process completed successfully')