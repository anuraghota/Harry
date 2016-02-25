__author__= 'Anurag'

user_information = {}


def set_name(name):
    global user_information
    user_information["name"] = name

def set_home_address(address):
    global user_information
    user_information["home_address"] = address

def set_office_address(address):
    global user_information
    user_information["office_address"] = address

def set_current_location(location):
    global user_information
    user_information["current_location"] = location

def set_age(age):
    global user_information
    user_information["age"] = age

def set_gender(gender):
    global user_information
    user_information["gender"] = gender

def set_current_marriage_status(marriage_status):
    global user_information
    user_information["marriage_status"] = marriage_status

def set_current_work_status(work_status):
    global user_information
    user_information["work_status"] = work_status

def get_name():
    global user_information
    name = user_information.get("name")
    if name is None:
        response= "You haven't told me yet!"
    else:
        response = name+"!I dont forget things so fast!"
    return response

def get_location():
    global user_information
    location = user_information.get("current_location")
    if location is None:
        response = "Some forces are stopping me to connect to your device. Cant find you."
    else:
        response = location
    return response

def get_gender():
    global user_information
    gender = user_information.get("gender")
    if gender is None:
        response= "Can you come closer to the camera? Let me have a look at you."
    else:
        response = "Ofcourse, You are a " + gender
    return response
