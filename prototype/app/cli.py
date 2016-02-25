import sys
import prototype.data.common_responses as response
import prototype.data.machine_questions as que
import prototype.data.user_data as user
from time import time
import msvcrt

def start():
    chat()

def chat():
    last_harry_message = None
    first_harry_greeting = "Hey!"
    print(first_harry_greeting)
    while True:
        user_message = str(input())
        last_harry_message = response.get_response(user_message)
        if last_harry_message == "name":
            last_harry_message = user.get_name()
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
            last_harry_message = user_message + "! Such a nice name!"
            print(last_harry_message)














