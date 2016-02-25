__author__='Anurag'

from user_data import user_information

def get_name():
    name = user_information.get("name")
    if name is None:
        name = "You haven't told me yet!"
    return name

responses = \
    {
        "hi": "Hello!Ssup",
        "what is your name": "Harry! Not Potter though. I am just Harry.",
        "what's your name": "Harry! Not Potter though. I am just Harry.",
        "who is your father": "Anurag! I love my daddy.",
        "who's your father": "Anurag! I love my daddy.",
        "who is your mother": "My dad is single.",
        "who's your mother": "My dad is single.",
        "say my name": get_name(),
        "what is my name": get_name(),
        "what's my name": get_name()
    }


def get_response(query):
    query = query.lower()
    response = responses.get(query)
    if response is None:
        response = "Didn't get you!My vocabulary is improving day by day."
    return response




if __name__ == '__main__':
    query = 'Say my name'
    result = get_response(query)
    print(result)


