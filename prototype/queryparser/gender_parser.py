__author__ = 'Anurag'

from genderize import Genderize

def get_gender(name):
    result = Genderize().get([name])[0].get("gender")
    if result is None:
        result = "unisex"
    return result

