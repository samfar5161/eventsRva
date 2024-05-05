#!/bin/bash

echo "Updating event schedules..."

echo "1. The National RVA..."
cd /srv/eventsrva_data/py_env/the_national_rva
./update_theNationalRVA_sched.sh

echo "2. The Funnybone RVA..."
cd /srv/eventsrva_data/py_env/the_funnybone_rva
./update_theFunnyBoneRVA_sched.sh


echo "All updates complete"
