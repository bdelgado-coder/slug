# Brandon Delgado
# Data Science Project #1
# Travelling Politician Problem

import pandas as pd
import mpu
import json
import sys
from itertools import permutations


def distance(lat1, long1, lat2, long2):
    dist = mpu.haversine_distance((lat1, long1), (lat2, long2))
    return dist


def cord(state_name):
    # Pulling zip code from dictionary
    zip = zipcodes[state_name]
    zip1 = data.loc[(data['ZipCode'] == zip)]

    longitude = zip1.iloc[0, 4]
    latitude = zip1.iloc[0, 3]

    return longitude, latitude

# Creates all possible permutations of the capitals
# Prerequisites: start & end are strings, middle must be a list
# Returns a list
def perm(start, middle, end):
    p = permutations(middle)
    for i in p:
        print(''.join(i))

    for i in p:
        i.prepend(start)

    for i in p:
        i.append(end)


# Dictionary of zip codes
zipcodes = {
    "AL": 36101,  # Alabama
    "AK": 99801,  # Alaska
    "AZ": 85001,  # Arizona
    "AS": 72201,  # Arkansas
    "CA": 94203,  # California
    "CO": 80201,  # Colorado
    "CT": 6101,  # Connecticut
    "DE": 19901,  # Delaware
    "FL": 32301,  # Florida
    "GA": 30301,  # Georgia
    "HI": 96801,  # Hawaii
    "ID": 83701,  # Idaho
    "IL": 62701,  # Illinois
    "IN": 46201,  # Indiana
    "IA": 50301,  # Iowa
    "KS": 66601,  # Kansas
    "KY": 40601,  # Kentucky
    "LA": 70801,  # Louisiana
    "ME": 4330,  # Maine
    "MD": 21401,  # Maryland
    "MA": 2108,  # Massachusetts
    "MI": 48901,  # Michigan
    "MN": 55101,  # Minnesota
    "MS": 39201,  # Mississippi
    "MO": 65101,  # Missouri
    "MT": 59601,  # Montana
    "NE": 68501,  # Nebraska
    "NV": 89701,  # Nevada
    "NH": 3301,  # New Hampshire
    "NJ": 8601,  # New Jersey
    "NM": 87501,  # New Mexico
    "NY": 12201,  # New York
    "NC": 27601,  # North Carolina
    "ND": 58501,  # North Dakota
    "OH": 43201,  # Ohio
    "OK": 73101,  # Oklahoma
    "OR": 97301,  # Oregon
    "PA": 17101,  # Pennsylvania
    "RI": 2901,  # Rhode Island
    "SC": 29201,  # South Carolina
    "SD": 57501,  # South Dakota
    "TN": 37201,  # Tennessee
    "TX": 73301,  # Texas
    "UT": 84101,  # Utah
    "VT": 5601,  # Vermont
    "VA": 23218,  # Virgina
    "WA": 98501,  # Washington
    "WV": 25301,  # West virgina
    "WI": 53701,  # Wisconsin
    "WY": 82001,  # Wyoming
    "DC": 20500  # Washington DC
}

# Import CSV file into data frame
data = pd.read_csv("zip_codes.csv")

# Opens the in file and stores the JSON obj as json_dict
with open('in.json', 'r') as f:
    in_dict = json.load(f)

# Storing the destinations in string variables
start = in_dict["start"]
end = in_dict["end"]

# Storing destinations in between as a list
middle = str.split(in_dict["middle"], ", ")

# Storing zip codes for each each state listed
zip_start = zipcodes.get(start)
zip_end = zipcodes.get(end)

# Stores the list of middle zipcodes
zip_middle = []
for i in middle:
    zip_middle.append(zipcodes.get(i))

print('Permutations List:')
perm(start, middle, end)
print('\n')

long1, lat1 = cord(start)
long2, lat2 = cord(end)

d = distance(lat1, long1, lat2, long2)
print('%.2f meters\n' % (d))
