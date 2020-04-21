# Brandon Delgado
# Data Science Project #1
# Travelling Politician Problem

import pandas as pd
import mpu
import json
import sys
import itertools

# Dictionary of zip codes
zip_code = {
    'Alabama': 36043,
    'Alaska': 99801,
    'Arizona': 85001,
    "Arkansas": 72201,
    "California": 94203,
    "Colorado": 80201,
    "Connecticut": 6101,
    "Delaware": 19901,
    "Florida": 32301,
    "Georgia": 30301,
    "Hawaii": 96801,
    "Idaho": 83701,
    "Illinois": 62701,
    "Indiana": 46201,
    "Iowa": 50301,
    "Kansas": 66601,
    "Kentucky": 40601,
    "Louisiana": 70801,
    "Maine": 4330,
    "Maryland": 21401,
    "Massachusetts": 2108,
    "Michigan": 48901,
    "Minnesota": 55101,
    "Mississippi": 39201,
    "Missouri": 65101,
    "Montana": 59601,
    "Nebraska": 68501,
    "Nevada": 89701,
    "New Hampshire": 3301,
    "New Jersey": 8601,
    "New Mexico": 87501,
    "New York": 12201,
    "North Carolina": 27601,
    "North Dakota": 58501,
    "Ohio": 43201,
    "Oklahoma": 73101,
    "Oregon": 97301,
    "Pennsylvania": 17101,
    "Rhode Island": 2901,
    "South Carolina": 29201,
    "South Dakota": 57501,
    "Tennessee": 37201,
    "Texas": 73301,
    "Utah": 84101,
    "Vermont": 5601,
    "Virginia": 23218,
    "Washington": 98501,
    "West Virginia": 25301,
    "Wisconsin": 53701,
    "Wyoming": 82001,
    "Washington D.C.": 20500
}

# Import CSV file into data frame
data = pd.read_csv ("zip_codes.csv")

# Opens the in file and stores the JSON obj as json_dict
in_read = open('in.json')
json_dict = json.load(in_read)
print(json_dict)

zip1 = 0
lat1 = 0
long1 = 0

zip2 = 0
lat2 = 0
long2 = 0

dist = mpu.haversine_distance((lat1,long1),(lat2,long2))

# Formats the string to print up to 100th place, and to include units
print( '%.2f meters\n' % (dist) )

