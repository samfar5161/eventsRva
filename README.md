# EventsRVA

## Description
This program compiles a list of events that are taking place at popular venues in Richmond, VA and plots them on a calendar for the user.
The program uees Python/BeautifulSoup to scrape the events pages of lpcal venues, creates a JSON file which is fed into the web application
and plots the calendar.

#### Current Venues:
1. The National RVA
2. The Funnybone - Shortpump

#### Venues In Progress:
1. The Broadberry venues

### Work in progress:
1. Adding details to the calendar view - such as opening act, link to ticket POS, etc.
2. Export to Google Calendars
3. Adding different vizualzations, such as week view and day view, which would plot different events taking place during a single day, allowing users to build their schedules more efficiently.


## File Structure
1. EventsRva
   a. This holds the javascript and web application files
   b. This holds the web server config file
   c. This holds a copy of the even JSON files for each venue

2. EventsRva_Data
  a. This holds the web scraping and JSON parsing scripts for each venue.
  b. This holds the scipts that update the JSON files in eventsRva folder.
  c. New venues will be added to this folder first.

# Feedback welcome!
