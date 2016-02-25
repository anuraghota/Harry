__author__='Anurag'

import wikipedia

def search(query):
    try:
        data = wikipedia.summary(query,sentences=2)
        return data
    except Exception as e:
        return None
