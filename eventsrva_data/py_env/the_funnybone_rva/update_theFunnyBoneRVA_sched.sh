#!/bin/bash

# execute the update script
cd /srv/eventsrva_data/py_env/the_funnybone_rva
sudo python3 get_data_from_fbrva.py

echo "copying file..."
# copy the new JSON file
sudo cp /srv/eventsrva_data/py_env/the_funnybone_rva/funnybone_events_output.json /srv/eventsrva/event_files/funnybone_events_output.json

# print line if successful
echo "Process completed successfully"

