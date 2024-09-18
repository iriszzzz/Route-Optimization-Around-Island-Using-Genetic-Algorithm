# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import googlemaps
import csv
import time

gmaps = googlemaps.Client(key='')   # '' includes your API key

# Define the center point and radius for the search
location = (22.613528351534722, 120.26862376634575)
radius = 10000  # meter

# Query tourist attractions within the specified radius
places_result = gmaps.places_nearby(location=location, keyword='tourist', radius=radius)
results = places_result['results']

# Fetch additional pages of results if available
while 'next_page_token' in places_result:
    time.sleep(2)
    places_result = gmaps.places_nearby(page_token=places_result['next_page_token'])
    results.extend(places_result['results'])

# Sort attractions by rating
results.sort(key=lambda x: x.get('rating', 0), reverse=True)

# Filter out attractions with a rating count less than 300
results_filtered = [place for place in results if place.get('user_ratings_total', 0) >= 100]

# Write attractions to CSV
with open('Kaohsiung_Tourist_2.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['name', 'latitude', 'longitude', 'rating', 'rating_count', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writeheader()

    # Query details for each attraction and write to CSV
    for i, place in enumerate(results_filtered[:80], 1):
        place_name = place['name']

        # Use geocoding API to get the Place ID of the attraction
        geocode_result = gmaps.geocode(place_name)
        if not geocode_result:
            print(f"Could not find location: {place_name}")
            continue

        place_id = geocode_result[0]['place_id']

        # Fetch details for the attraction
        place_details = gmaps.place(place_id=place_id, fields=['name', 'rating', 'user_ratings_total', 'geometry', 'formatted_address'])

        if 'result' in place_details:
            result = place_details['result']
            place_name = result.get('name')
            rating = result.get('rating', 'N/A')
            rating_count = result.get('user_ratings_total', 'N/A')
            location = result['geometry']['location']
            address = result.get('formatted_address', 'N/A')

            # Write data to CSV
            writer.writerow({
                'name': place_name,
                'latitude': location['lat'],
                'longitude': location['lng'],
                'rating': rating,
                'rating_count': rating_count,
                'address': address
            })

            print(f"{i}: {place_name} - Rating: {rating}, Rating Count: {rating_count}, Address: {address}, Location: ({location['lat']}, {location['lng']})")
        else:
            print(f"Could not retrieve place details for {place_name}")
