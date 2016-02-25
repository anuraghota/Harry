import prototype.data.common_responses as response
import prototype.data.machine_questions as que
import prototype.data.user_data as user
import prototype.queryparser.gender_parser as genderparser
internet_check = False

def start():
    set_location()
    chat()

def set_location():
    import urllib.request
    import json
    try:
        print("Loading...")
        f = urllib.request.urlopen('http://freegeoip.net/json/')
        json_string = f.read()
        f.close()
        location = json.loads(json_string)
        city = location.get("city")
        state = location.get('region_name')
        country = location.get('country_name')

        location_result = city
        if state is not None:
            location_result = location_result + ", " + state
        if country is not None:
            location_result = location_result + ", " + country
        user.set_current_location(location_result)
        global internet_check
        internet_check = True
    except Exception as e:
        pass

def chat():
    last_harry_message = None
    global internet_check
    if internet_check:
        first_harry_greeting = "Hey!"
    else:
        first_harry_greeting = "Dude, your internet sucks!\nAnyways Hello!!"
    print(first_harry_greeting)
    while True:
        user_message = str(input())
        last_harry_message = response.get_response(user_message)
        if last_harry_message == "name":
            last_harry_message = user.get_name()
        elif last_harry_message == "location":
            last_harry_message = user.get_location()
        elif last_harry_message == "gender":
            last_harry_message = user.get_gender()
        print(last_harry_message)
        if user_message.lower() == 'bye':
            break

        if que.question_tags.get("name"):
            pass
        else:
            last_harry_message = que.questions.get("name")
            print(last_harry_message)
            user_message = str(input())
            que.set_tag("name")
            user.set_name(user_message)
            last_harry_message = user_message + "! Such a nice name."
            print(last_harry_message)
            gender = genderparser.get_gender(user_message)
            que.set_tag("gender")
            user.set_gender(gender)
            if gender == 'male':
                last_harry_message = "Ah! Male.Nice Bhai Bhai"
            else:
                last_harry_message = "Oh! Girl! You could be my girlfriend!"
            print(last_harry_message)
