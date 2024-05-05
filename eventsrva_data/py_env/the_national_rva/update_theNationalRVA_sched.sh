#!/bin/bash

# execute the update script
cd /srv/eventsrva_data/py_env/the_national_rva
sudo python3 get_data_from_the_national.py

echo "copying file..."
# copy the new json file
sudo cp /srv/eventsrva_data/py_env/the_national_rva/TheNational_events_output.json /srv/eventsrva/event_files/TheNational_events_output.json

# print line if successful
echo "process completed successfully"
