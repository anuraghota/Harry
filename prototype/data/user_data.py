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
