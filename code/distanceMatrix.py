# -*- coding: utf-8 -*-
"""
Created on Thu May 16 03:28:20 2024

@author: User
"""
import numpy as np
import pandas as pd
import googlemaps
import csv
import time

gmaps = googlemaps.Client(key='')   # '' includes your API key

# Read attractions from CSV
df = pd.read_csv('Kaohsiung_Tourist_2.csv')
distances = []

# Calculate distances between attractions
for i in range(10):
    row = []
    for j in range(10):
        if i == j:
            row.append(0)
        else:
            origin = df.loc[i, 'address']
            destination = df.loc[j, 'address']
            result = gmaps.distance_matrix(origin, destination)

            if 'distance' in result['rows'][0]['elements'][0]:
                distance = result['rows'][0]['elements'][0]['distance']['text']
                row.append(distance)
            else:
                row.append(None)
    distances.append(row)

# Print distances matrix
for row in distances:
    print(row)