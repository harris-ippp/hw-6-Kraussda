#!/usr/bin/env python 

import requests
from bs4 import BeautifulSoup as bs

# For simplicity I duplicated the e1 work here.

resp = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General")

html = resp.content

soup = bs(html, "html.parser")

tags = soup.find_all('tr','election_item')

ids = [tags[x]['id'][-5:] for x in range(24)]

years = [tags[x].contents[1].text for x in range(24)]

dictionary = dict(zip(ids, years))


# Create a base URL in which to plug in ids
base = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"


# Loop over ids and create csv's of the format "year.csv" containing the data for that year.
for i in ids:
    resp = requests.get(base.format(i))
    file_name = dictionary[i] +".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)
