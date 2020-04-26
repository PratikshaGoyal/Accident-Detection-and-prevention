#!/usr/bin/env python
# coding: utf-8

from googleplaces import GooglePlaces, types, lang
import sms
import gps

con = []

def contact():
    return con

def nearby():
    # Use your own API key for making api request calls 
    API_KEY = 'your API Key'
      
    # Initialising the GooglePlaces constructor 
    google_places = GooglePlaces(API_KEY) 
    # fix location
    # latitude = 27.568891
    # longitude = 76.640637  
    
    location = gps.location()
    latitude = location[0]
    longitude = location[1]
    # call the function nearby search with the parameters as longitude, latitude, radius
    # and type of place which needs to be searched of
    nearby_hospital = google_places.nearby_search(
            lat_lng ={'lat': latitude, 'lng': longitude}, 
            types =[types.TYPE_HOSPITAL])  

    nearby_police = google_places.nearby_search(
            lat_lng ={'lat': latitude, 'lng': longitude}, 
            types =[types.TYPE_POLICE])  


    for i, j in zip(nearby_hospital.places, nearby_police.places): 
        print (i.name)
        print("Latitude =",i.geo_location['lat']) 
        print("Longitude =",i.geo_location['lng'])
        i.get_details()
        print("Phone no. =", i.international_phone_number)
        con.append(i.international_phone_number)
        print()
        
        print (j.name)
        print("Latitude =",j.geo_location['lat']) 
        print("Longitude =",j.geo_location['lng'])
        j.get_details()
        print("Phone no. =", j.international_phone_number)
        con.append(j.international_phone_number)
        print()
        break
    sms.sms(latitude,longitude)
