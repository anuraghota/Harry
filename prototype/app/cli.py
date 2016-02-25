import sys
import prototype.data.common_responses as response
def start():
    chat()

def chat():
    last_harry_message = None
    first_harry_greeting = "Hey!"
    print(first_harry_greeting)
    while True:
        user_message = str(input())
        last_harry_message = response.get_response(user_message)
        print(last_harry_message)





