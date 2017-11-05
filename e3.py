#!/usr/bin/env python 

import pandas as pd


# Making the base year dataframe

name = "1924" + ".csv"
header = pd.read_csv(name, nrows = 1).dropna(axis = 1)
d = header.iloc[0].to_dict()

df = pd.read_csv(name, index_col = 0, thousands = ",", skiprows = [1])

df.rename(inplace = True, columns = d) # rename to democrat/republican
df.dropna(inplace = True, axis = 1)    # drop empty columns
df = df[['Republican','Total Votes Cast']] # Keep only relevant data for the graph
df["Year"] = 1924

# Appending the remaining years to that
years = [1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]

for year in years:
    name = str(year) + ".csv"
    header = pd.read_csv(name, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    dftemp = pd.read_csv(name, index_col = 0, thousands = ",", skiprows = [1])

    dftemp.rename(inplace = True, columns = d) # rename to democrat/republican
    dftemp.dropna(inplace = True, axis = 1)    # drop empty columns
    dftemp = dftemp[['Republican','Total Votes Cast']] # Keep only relevant data for the graph
    dftemp["Year"] = year
    df = df.append(dftemp)

# Defining Republican Share

df["Republican Share"]= df["Republican"]/df["Total Votes Cast"]

# Masking out the important counties
dfAccomack = df.loc['Accomack County']
dfAlbemarle = df.loc['Albemarle County'] # Albemarle County is missing data from 1992
dfAlexandria = df.loc['Alexandria City']
dfAlleghany = df.loc['Alleghany County']

# Making Plots

ax = dfAccomack.plot(x = "Year", y = "Republican Share", legend = False, title = "Accomack County Historical Election Results")
ax.set_ylabel("Republican Vote Share")
ax.figure.savefig("accomack_county.pdf")
ax = dfAlbemarle.plot(x = "Year", y = "Republican Share", legend = False, title = "Albemarle County Historical Election Results")
ax.set_ylabel("Republican Vote Share")
ax.figure.savefig("albemarle_county.pdf")
ax = dfAlexandria.plot(x = "Year", y = "Republican Share", legend = False, title = "Alexandria City Historical Election Results")
ax.set_ylabel("Republican Vote Share")
ax.figure.savefig("alexandria_city.pdf")
ax = dfAlleghany.plot(x = "Year", y = "Republican Share", legend = False, title = "Alleghany County Historical Election Results")
ax.set_ylabel("Republican Vote Share")
ax.figure.savefig("alleghany_county.pdf")


