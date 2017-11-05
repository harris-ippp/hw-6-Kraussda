#!/usr/bin/env python 

import requests
from bs4 import BeautifulSoup as bs


# Pull data from the site with the table and parse it as html

resp = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General")

html = resp.content

soup = bs(html, "html.parser")

# Grab just the table rows with election data

tags = soup.find_all('tr','election_item')

# Grab the numeric part of the ids

ids = [tags[x]['id'][-5:] for x in range(24)]

# Return the td that contains the year

years = [tags[x].contents[1].text for x in range(24)]

# Print the year and ids

print(years, ids)

# Create a year/id dictionary

dictionary = dict(zip(ids, years))