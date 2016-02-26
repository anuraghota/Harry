__author__ = 'Anurag'
ACCESS_TOKEN = "YOUR_TOEN_HERE"

import requests
import json

def build_URL(search_text='',types_text=''):
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    key_string = '?key='+ ACCESS_TOKEN
    query_string = '&query='+ search_text
    sensor_string = '&sensor=false'
    type_string = ''
    if types_text!='':
        type_string = '&types='+ types_text
    url = base_url+key_string+query_string+sensor_string+type_string
    return url

def get_results(type):
    url = build_URL(search_text='Jubilee Hills',types_text=type)
    response = requests.get(url)
    result = return_results(response.text)
    return result

def return_results(query):
    response = []
    query = json.loads(query)
    results = query.get("results")
    for doc in results:
        if doc.get("name") not in response:
            response.append(doc.get("name"))
    return response
